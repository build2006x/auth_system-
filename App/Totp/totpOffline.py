# main.py
import io
import pyotp
import qrcode
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from App.Totp.Database import SessionLocal, User, engine, Base, UserCreate, get_db

apps = APIRouter(prefix="/OfflineVerifcation",tags=["VerifyTotp"])

# Register user + generate QR
@apps.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # check if user already exists
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    # generate secret
    secret = pyotp.random_base32()
    db_user = User(username=user.username, totp_secret=secret)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    # provisioning URI
    uri = pyotp.TOTP(secret).provisioning_uri(
        name=user.username,
        issuer_name="HackathonPortal"
    )

    # QR code
    qr = qrcode.make(uri)
    buf = io.BytesIO()
    qr.save(buf)
    buf.seek(0)

    return StreamingResponse(buf, media_type="image/png")


# Verify OTP
@apps.get("/verify/{username}")
def verify_code(username: str, code: str, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == username).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    totp = pyotp.TOTP(str(db_user.totp_secret))
    if totp.verify(str(code), valid_window=1):  # cast to str for safety
        return {"status": "success", "message": "OTP verified"}
    else:
        raise HTTPException(status_code=400, detail="Invalid OTP")

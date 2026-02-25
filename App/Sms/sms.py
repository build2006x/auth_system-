from fastapi import HTTPException
from twilio.rest import Client
from fastapi import APIRouter,Query
from dotenv import load_dotenv
import os
from pydantic import BaseModel


load_dotenv()

api =  APIRouter()

account_sid = os.getenv("Twilio_Sid")
account_token = os.getenv("Twilio_token")
account_service = os.getenv("Twilio_Service_id")

client = Client(account_sid,account_token)

@api.post("/send_otp")
def send_Otp(PhoneNumber:int):
    try:
        verification = client.verify.services(str(account_service)).verifications.create(
            to=f"+91{str(PhoneNumber)}", channel="sms"
        )
        return {"status": verification.status}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

def verify_otp(phone: str, code: str):
    try:
        verification_check = client.verify.services(str(account_service)).verification_checks.create(
            to=phone, code=code
        )
        return {"status": verification_check.status}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# @api.post("/verify_otp")
# async def verify_endpoint(phone:str=Query(...),code:str=Query(...)):
#           result = verify_otp(phone,code)
#           if result['status'] == "approved":
#                   existing_user = getuserPhone(phone)    
#                   if existing_user:
#                        return               
#           else:
#                return { 
#                 "status": result["status"],
#                 "message": result.get("message", "OTP verification failed"),
#                 "user_exists": False
#             }
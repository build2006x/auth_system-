### gmail sending to the person
from fastapi import APIRouter
import smtplib
import random 
from email.mime.text import MIMEText
from pydantic import BaseModel,EmailStr

### this for writing the gamil sending 

router = APIRouter(prefix="/Gmail",tags=["Gmailapi"])

### pydantic for email vaildator 
class email(BaseModel):
      email:EmailStr
     
## endpoint for sending the gamil info 

@router.post("/EmailSend")
async def sendCode(Email:email):
        ### intializing the sms presetup 
        # Hardcoded email details 
        sender_email = "mabarathkumar@gmail.com" 
        sender_password = "ykvy qqnw cwev vfyi" 
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        ### generating the four code for the otp 
        code = str(random.randint(1000, 9999))
        msg = MIMEText(f"Your verification code is: {code}") 
        msg["Subject"] = "Verification Code"
        msg["From"] = "mabarathkumar@gmail.com"
        msg["To"] = Email.email

        try: 
           # Connect to SMTP server 
           server = smtplib.SMTP(smtp_server, smtp_port) 
           server.starttls() 
           server.login(sender_email, sender_password) 
           server.sendmail(sender_email, [Email.email], msg.as_string()) 
           server.quit()
           return {"status": "success", "code_sent": code} 
        except Exception as e: 
             return {"status": "error", "details": str(e.message)}




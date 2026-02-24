from fastapi import FastAPI
# from .EmailFile.gmailSender import router
from App.VoiceFile.VioceCall import VoiceRouter
from App.Totp.totpOffline import apps
from App.Sms.sms import api


main  = FastAPI()


### setup the middleware for the frontend to the acess the function in the backend logic 

from fastapi.middleware.cors import CORSMiddleware
main.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# main.include_router(router)
main.include_router(api)
main.include_router(VoiceRouter)
main.include_router(apps)


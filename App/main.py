from fastapi import FastAPI
# from .EmailFile.gmailSender import router
from App.VoiceFile.VioceCall import VoiceRouter
from App.Totp.totpOffline import apps
from App.Sms.sms import api


main  = FastAPI()

# main.include_router(router)
main.include_router(api)
main.include_router(VoiceRouter)
main.include_router(apps)


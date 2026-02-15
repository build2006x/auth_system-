from fastapi import FastAPI
# from .EmailFile.gmailSender import router
from App.Totp.totpOffline import apps
from App.VoiceFile.VioceCall import VoiceRouter

main  = FastAPI()

# main.include_router(router)
main.include_router(VoiceRouter)
main.include_router(apps)

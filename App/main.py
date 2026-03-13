from fastapi import FastAPI
# from .EmailFile.gmailSender import router
from App.VoiceFile.VioceCall import VoiceRouter
from App.Totp.totpOffline import apps
from App.Sms.sms import api
from fastapi.middleware.cors import CORSMiddleware
from App.EmailFile.gmailSender import router


app  = FastAPI()

# Allowed frontend origins
origins = [
    "http://localhost:5173",   # Local React development
    "my-react-beta-fawn.vercel.app"

]

# CORS Middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # Allow specific origins
    allow_credentials=True,
    allow_methods=["*"],        # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],        # Allow all headers
)


# app.include_router(router)
app.include_router(api)
app.include_router(router)
app.include_router(VoiceRouter)
app.include_router(apps)


@app.get("/")
def hell0():
    return "checking the deployment of the backend code"

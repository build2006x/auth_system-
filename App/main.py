from fastapi import FastAPI
# from .EmailFile.gmailSender import router
from App.VoiceFile.VioceCall import VoiceRouter
from App.Totp.totpOffline import apps
from App.Sms.sms import api
from fastapi.middleware.cors import CORSMiddleware
from App.EmailFile.gmailSender import router

app  = FastAPI()
# origins = [
#     "http://localhost:5173",
#     "http://127.0.0.1:5173",
#     "https://my-react-beta-fawn.vercel.app",
#     "https://my-react-jz5dcmbea-barath-kuamars-projects.vercel.app",
#     "*",
# ]


### setup the middleware for the frontend to the acess the function in the backend logic 



from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(router)
app.include_router(api)
app.include_router(router)
app.include_router(VoiceRouter)
app.include_router(apps)


@app.get("/")
def hell0():
    return "checking the deployment of the backend code"

from fastapi import APIRouter
import pyttsx3
import random
import asyncio
import sys
from concurrent.futures import ThreadPoolExecutor

VoiceRouter = APIRouter(prefix="/tts", tags=["TTS"])
executor = ThreadPoolExecutor(max_workers=1)

def speak(text: str):
    if sys.platform == 'win32':
        engine = pyttsx3.init('sapi5')
    else:
        engine = pyttsx3.init()
    
    # <-- IMPORTANT: create fresh
    voices = list(engine.getProperty('voices'))
    if len(voices) > 1:
        engine.setProperty('voice', voices[2].id)
    elif voices:
        engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate',120)

    engine.say(text)
    engine.runAndWait()
    engine.stop()  
    ### this will stop the server 

@VoiceRouter.get("/speak")
async def speak_random_number():
    number = random.randint(100, 999)
    text = f"Your verification number is {number}"

    loop = asyncio.get_running_loop()

    try:
        await asyncio.wait_for(
            loop.run_in_executor(executor, speak, text),
            timeout=6
        )
       
    except asyncio.TimeoutError:
        return {"error": "TTS timeout"}
    return {"code_sent":number}

   




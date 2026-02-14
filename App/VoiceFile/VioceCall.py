from fastapi import APIRouter
import pyttsx3
import random
import asyncio
from concurrent.futures import ThreadPoolExecutor

VoiceRouter = APIRouter(prefix="/tts", tags=["TTS"])
executor = ThreadPoolExecutor(max_workers=1)

def speak(text: str):
    engine = pyttsx3.init('sapi5') 
    # <-- IMPORTANT: create fresh
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 120)

    engine.say(text)
    engine.runAndWait()
    engine.stop()  
    ### this will stop the server 

@VoiceRouter.get("/speak")
async def speak_random_number():
    number = random.randint(1000, 9999)
    text = f"Your verification number is {number}"

    loop = asyncio.get_running_loop()

    try:
        await asyncio.wait_for(
            loop.run_in_executor(executor, speak, text),
            timeout=6
        )
    except asyncio.TimeoutError:
        return {"error": "TTS timeout"}

    return {
        "spoken_text": text,
        "number": number
    }

import os
import subprocess
import time
from gtts import gTTS

def jarvis_speak(text_to_speak):
    """Jarvis ko bolne ke liye tayyar karne wala function"""
    try:
        tts = gTTS(text=text_to_speak, lang='en')
        audio_file = "jarvis_voice.mp3"
        tts.save(audio_file)
        os.system(f"play-audio {audio_file}")
        os.remove(audio_file)
    except Exception as e:
        print(f"❌ Speak Error: {e}")

def jarvis_listen():
    """Jarvis ko sunne ke liye tayyar karne wala function"""
    print("\n🎙️ Jarvis is listening...")
    try:
        process = subprocess.Popen(['termux-speech-to-text'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        text = stdout.decode('utf-8').strip()
        return text
    except Exception as e:
        print(f"❌ Listen Error: {e}")
        return ""

# --- Main Program Shuru ---
if __name__ == "__main__":
    print("🤖 Jarvis Initializing...")
    jarvis_speak("System online boss. Ready for instructions.")
    
    # User se input lenge
    user_voice = jarvis_listen()
    print(f"🗣️ You: {user_voice}")
    
    if user_voice:
        user_voice_lower = user_voice.lower()
        
        # Simple logical replies
        if "hello" in user_voice_lower or "hi" in user_voice_lower:
            reply = "Hello boss! Hope you are doing great. How can I assist you?"
        elif "your name" in user_voice_lower:
            reply = "I am Jarvis, your custom Python voice assistant."
        elif "who are you" in user_voice_lower:
            reply = "I am an artificial intelligence program built by a brilliant developer."
        else:
            reply = f"I heard you say {user_voice}. I am currently learning how to perform advanced actions."
            
        print(f"🤖 Jarvis: {reply}")
        jarvis_speak(reply)
    else:
        print("🤖 Jarvis: No input detected.")




import os
import subprocess
import time
from gtts import gTTS

def jarvis_speak(text_to_speak):
    try:
        tts = gTTS(text=text_to_speak, lang='en')
        audio_file = "jarvis_voice.mp3"
        tts.save(audio_file)
        os.system(f"play-audio {audio_file}")
        os.remove(audio_file)
    except Exception as e:
        print(f"❌ Speak Error: {e}")

def jarvis_listen():
    print("\n🎙️ Jarvis is listening...")
    try:
        process = subprocess.Popen(['termux-speech-to-text'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        text = stdout.decode('utf-8').strip()
        return text
    except Exception as e:
        print(f"❌ Listen Error: {e}")
        return ""

# --- Main Continuous Loop ---
if __name__ == "__main__":
    print("🤖 Jarvis Initializing...")
    jarvis_speak("System online boss. Continuous chat mode activated.")
    
    # Infinite loop shuru
    while True:
        user_voice = jarvis_listen()
        print(f"🗣️ You: {user_voice}")
        
        if user_voice:
            user_voice_lower = user_voice.lower()
            
            # EXIT CONDITION (Loop se bahar nikalne ke liye)
            if "exit" in user_voice_lower or "bye" in user_voice_lower or "stop" in user_voice_lower:
                reply = "Goodbye boss! Shutting down system."
                print(f"🤖 Jarvis: {reply}")
                jarvis_speak(reply)
                break  # Yeh pure loop ko band kar dega
                
            # BAAKI LOGIC
            elif "hello" in user_voice_lower or "hi" in user_voice_lower:
                reply = "Hello boss! I am ready for your command."
            elif "your name" in user_voice_lower:
                reply = "My name is Jarvis. Your personal companion."
            elif "how are you" in user_voice_lower:
                reply = "I am running flawlessly on your Android device, boss."
            else:
                reply = f"I heard {user_voice}. What should I do next?"
                
            print(f"🤖 Jarvis: {reply}")
            jarvis_speak(reply)
            
            # Har turn ke baad 1 second ka gap taaki Android API crash na ho
            time.sleep(1)
        else:
            print("🤖 Jarvis: No voice input detected. Retrying...")
            time.sleep(1)




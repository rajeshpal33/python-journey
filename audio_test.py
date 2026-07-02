import os
from gtts import gTTS

print("Testing the Google TTS Engine... 🔊")

text_to_speak = "System Online Boss. Ready for instructions."

try:
    # 1. Text ko voice (audio) mein convert kiya
    tts = gTTS(text=text_to_speak, lang='en')
    
    # 2. save audio in a temporary file
    audio_file = "welcome.mp3"
    tts.save(audio_file)
    print("Audio fike generated successfully...")
    
    print("Listen! ...")
    os.system(f"play-audio {audio_file}")
    
    # 3. After execution delete the temporary file 
    os.remove(audio_file)

except Exception as e:
    print(f"❌ Error aaya bhai: {e}")


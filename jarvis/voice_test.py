import subprocess
import time

def listen_to_user():
    print("\n🤖 Jarvis Smart Voice Input Engine...")
    print("Say something... Android voice window is opening! 🎙️")
    
    try:
        # Command run ki aur data lia
        process = subprocess.Popen(['termux-speech-to-text'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        
        # Audio se text convert decode kiya
        text = stdout.decode('utf-8').strip()
        
        if text:
            print(f"\n🗣️ You said: {text}")
            return text
        else:
            print("\n❌ Window directly closed or no text recognized.")
            return None
            
    except Exception as e:
        print(f"\n❌ Something went wrong: {e}")
        return None

# Ek chhota sa test loop taaki hum dekh sakein lamba bolne par kya hota hai
if __name__ == "__main__":
    user_input = listen_to_user()
    
    if user_input:
        print("--- Processing Input ---")
        if "hello" in user_input.lower():
            print("🤖 Jarvis: Hello Bhai! How can I help you today?")
        else:
            print(f"🤖 Jarvis: I heard you say '{user_input}', implementing next phase soon!")


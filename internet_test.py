import requests

print("Extracting an amazing programming quote from internet... 🌐")

# GitHub  official Zen API
url = "https://api.github.com/zen"

try:
    response = requests.get(url, timeout=5) # 5 second ka wait timer
    
    line = response.text
    
    print("\n📜 GitHub Zen Says:")
    print(f'"{line}"')

except Exception as e:
    print("\n❌ something went wrong!")
    print(f"Real error was: {e}")


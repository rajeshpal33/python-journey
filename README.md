# 🐍 Python Programming & Software Development Journey

Welcome to my core Python learning repository. Yeh space meri poori Python coding journey, scripts, aur advanced projects ko track karne ke liye hai.

## 🎯 Project Objectives
- **Foundational Excellence:** Python syntax, data structures, aur core logic ko scratch se seekhna.
- **Automation & Scripting:** Real-world workflows aur system automation scripts design karna.
- **Advanced Implementations:** External APIs, speech engines, aur file systems ko integrate karna.

## 🗺️ Learning Roadmap & Progress

### 🔹 Phase 1: Core Fundamentals
- [x] Variables, Data Types, aur Input/Output Operations
- [x] Control Flow (If-Else) aur Structural Logic
- [x] Functions (`def`), Arguments, aur Return Modifiers
- [x] Python Lists, Tuples, aur Dictionary Management

### 🔹 Phase 2: System Data & File Handling
- [x] File Operations (Reading, Writing, and Appending)
- [x] Working with Context Managers (`with open()`)
- [ ] Data Persistence (Handling JSON and CSV files)

### 🔹 Phase 3: External Ecosystem & Advanced Tools
- [x] Package Management using `pip`
- [x] Integrating Standard & External Libraries (Requests & gTTS)
- [x] Building Interactive CLI (Command Line) Tools
- [x] Capstone Project: Voice-Enabled Automation Assistant (Jarvis)

---

## 🛠️ Project Showcase: Jarvis Voice Assistant
An interactive, continuous voice-controlled AI assistant built entirely in Python on an Android device using Termux. Jarvis can speak to you and listen to your voice commands in real-time.

### 🚀 Features
- **Continuous Conversation:** Runs on an infinite `while True` loop until safely exited.
- **Voice Recognition (Hearing):** Integrated with Android's native Google Voice Engine using `termux-speech-to-text`.
- **Text-to-Speech (Speaking):** Converts Python responses into clear audio via the `gTTS` library.
- **Smart Decision Tree:** Processes inputs case-insensitively and replies dynamically based on keywords.

### 📁 Folder Structure
- `jarvis/` - Core project folder.
  - `main.py` - The master script running the continuous speech loop.
- `internet_test.py` - Script to verify connectivity before booting modules.

### 🏃 How to Run Jarvis
```bash
cd jarvis
python main.py



# Calyx — Personal AI Agent

Calyx is a Python-based personal AI assistant built by Tamim.

It can chat with you, answer questions using AI, remember things, open apps/websites, fetch live weather/news, and now even speak back using voice.

**Current Version:** v2.0 (GUI + Smart Search)

---

## What Can Calyx Do?

### Talk Like an AI Assistant
- Natural conversation
- Personality-based replies
- AI-powered answers using LLM
- Smart web search fallback

Example:
```bash
You: what is a black hole
Calyx: A black hole is a region in space where gravity is so strong that even light cannot escape.

You: who is the current president of France
Calyx: (Searches the web and answers with the latest information.)
```
```

---

### Remember Things
Calyx can store information and recall it later.

Examples:
```bash
remember my name
show notes
search memory
forget
```

---

### Productivity Tools
- Calculator
- To-do list
- Notes
- Time & Date

Example:
```bash
You: time
Calyx: 10:45 PM
```

---

### Open Apps & Websites
Calyx can launch apps and websites for you.

Examples:
```bash
open youtube
open google
open vscode
```

Supported apps/websites:
- YouTube
- Google
- Facebook
- Instagram
- Chrome
- VS Code
- Notepad
- Calculator
- Command Prompt
- File Explorer

---

### Live Information
Using APIs and smart web search, Calyx can fetch real-time information.

- Weather
- News
- Web Search

Example:
```bash
weather of dhaka
news of sports in us
```

---

### Voice Output
Calyx can speak its replies using Text-to-Speech.

Example:
```bash
You: hello
Calyx: Hey! What can I do for you?
```

---

### Voice Input
Calyx can listen to your voice and execute commands.

Example:
```bash
You: (Speak) Open YouTube
Calyx: Opening YouTube...
```
---

### Graphical User Interface (GUI)

Calyx now includes a desktop GUI for chatting instead of only using the terminal.

Features:

- Chat window
- Message history
- User & assistant chat bubbles
- Scrollable conversation
- Text input box
- Send button

> GUI is currently built using **Tkinter**.

---

# Tech Stack

- Python
- OOP
- JSON Storage
- REST APIs
- Groq API (Llama)
- Edge TTS
- Tkinter
- Selenium
- SpeechRecognition
- Tavily Search API
- psutil

---

# Installation

## Clone Repository
```bash
git clone https://github.com/tamim-707/Calyx.git
cd Calyx
```

## Install Dependencies
```bash
pip install -r requirements.txt
```

---

# Run Calyx

```bash
python main.py
```

---

# Project Structure

```bash
Calyx/
│
├── API/
├── Brain/
├── Commands/
├── GUI/
├── LLM/
├── Memory/
├── Utils/
│
├── main.py
├── gui.py
├── requirements.txt
└── README.md
```

---

# Development Progress

### Phase 1 — Core System ✅
- Command system
- Memory
- Notes
- Calculator

### Phase 2 — Architecture Upgrade ✅
- OOP structure
- Modular design
- Better routing

### Phase 3 — Assistant Upgrade ✅
- Weather API
- News API
- To-do list
- Voice output

### Phase 4 — AI Brain ✅
- Groq LLM integration
- Smart fallback responses

### Phase 5 — Desktop Experience ✅
- Tkinter GUI
- Chat interface
- Voice input
- Smart web search
- Improved user experience

---

# Future Plans

- Better memory
- Mobile support
- Autonomous AI agent
- Local LLM support

---

# Goal

My goal is to turn Calyx into a real personal AI agent similar to Siri or Jarvis — capable of conversation, reasoning, memory, and task execution.

---

# Author

**Tamim (tamim-707)**  
GitHub: https://github.com/tamim-707

---

**Status:** Active Development 🚀
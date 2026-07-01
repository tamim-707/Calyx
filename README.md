# # Calyx — Python AI Agent

Calyx is a Python-based personal AI assistant built by Tamim.

It combines rule-based commands, memory, APIs, and LLM capabilities to create a smart desktop assistant that can answer questions, remember information, and perform useful tasks.

Current Version: **v1.0**

---

## Features

### Core Assistant
- Greeting system
- Help menu
- Natural conversation
- Personality-based responses
- Exit / goodbye system

### Memory System
- Remember user information
- Store notes
- Save preferences
- Search memory
- Priority-based memory
- Forget system

### Productivity Tools
- Calculator
- To-do list
- Notes system
- Time & Date

### App / Web Launcher
Open apps and websites directly:
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

### APIs
- Weather API
- News API

### LLM Integration
Calyx can answer general knowledge questions using LLMs:
- Groq API (Llama)

Examples:
```bash
You: what is a black hole
You: who is trump
```

### Architecture Improvements
- Refactored using OOP
- Modular folder structure
- Command routing system
- Separate memory/storage layer
- LLM fallback for unknown commands

---

# Project Structure

```bash
Calyx/
│
├── main.py
│
├── Brain/
│   └── brain.py
│
├── Commands/
│   ├── basic.py
│   ├── web_app_open.py
│   ├── calculator.py
│   ├── todo.py
│   ├── news.py
│   ├── weather.py
│   ├── note_preference.py
│   └── name_remember_me.py
│
├── Memory/
│   ├── memory.json
│   └── storage.py
│
├── LLM/
│   ├── gemini_api.py
│   └── groq_api.py
│
├── config.py
├── .env
└── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/tamim-707/Calyx.git
cd Calyx
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install requests python-dotenv groq google-generativeai
```

---

# Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_key_here
GEMINI_API_KEY=your_key_here
NEWS_API_KEY=your_key_here
```

Never upload `.env` to GitHub.

Add to `.gitignore`:

```gitignore
.env
__pycache__/
*.pyc
```

---

# How to Run

```bash
python main.py
```

Example:

```bash
Hey there! Calyx v1.0 here.....
You: hi
Calyx: Ah, my favorite human is back.
```

---

# Example Commands

## Basic

```bash
hello
help
bye
```

## Time & Date

```bash
time
date
```

## Calculator

```bash
calc
```

Example:

```bash
Question: 3+4+2
Answer is 9
```

## Weather

```bash
weather of dhaka
```

## News

```bash
news of sports in us
```

## Memory

```bash
remember my name
show notes
search memory
forget
```

## Open Apps

```bash
open youtube
open google
open vscode
```

## LLM Questions

```bash
what is quantum physics
who is elon musk
how do black holes form
```

---

# Tech Stack

- Python
- OOP
- JSON Storage
- REST APIs
- Gemini API
- Groq API
- LLM Prompting

---

# Development Timeline

### Phase 1
- Basic command system
- Memory
- Notes
- Calculator

### Phase 2
- Refactor into modules
- OOP architecture
- Better storage

### Phase 3
- Weather API
- News API
- To-do list

### Phase 4
- LLM integration
- Gemini support
- Groq support

---

# Future Plans

Planned upgrades for Calyx:

- Voice input
- Voice output (TTS)
- Better intent router
- Context-aware memory
- GUI version
- Autonomous AI agent features
- Tool calling
- Local LLM support (Ollama)

---

# Goal of Calyx

The long-term goal is to turn Calyx into a powerful personal AI agent capable of:

- Natural conversation
- Reasoning
- Memory
- Tool use
- Automation
- Task execution

---

# Author

**Tamim (tamim-707)**  
Creator of Calyx

GitHub: https://github.com/tamim-707

---

# Status

Actively under development.
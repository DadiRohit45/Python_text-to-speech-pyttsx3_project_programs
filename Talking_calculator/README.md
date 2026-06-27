# 🧮 Voice-Enabled Calculator

A Python-based interactive calculator with **text-to-speech** support, allowing users to perform mathematical calculations through voice feedback and text input.

---

## 📋 Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Overview](#code-overview)
- [Security Note](#security-note)
- [Known Limitations](#known-limitations)
- [Future Improvements](#future-improvements)

---

## ✨ Features

- 🔊 **Voice feedback** — speaks prompts, results, and errors aloud using `pyttsx3`
- ➕ **Mathematical expressions** — supports `+`, `-`, `*`, `/`, `**`, `%`, `//`, and parentheses
- 🔁 **Continuous calculation** — chain multiple calculations in one session
- ❌ **Error handling** — invalid expressions are caught and reported gracefully
- 💬 **Interactive prompts** — guides the user step-by-step through voice instructions

---

## 🛠️ Requirements

- Python 3.6+
- [`pyttsx3`](https://pypi.org/project/pyttsx3/) — offline text-to-speech engine

---

## 📦 Installation

1. **Clone or download** the repository:
   ```bash
   git clone https://github.com/your-username/voice-calculator.git
   cd voice-calculator
   ```

2. **Install dependencies:**
   ```bash
   pip install pyttsx3
   ```

3. **Run the program:**
   ```bash
   python calculator.py
   ```

---

## 🚀 Usage

1. Run the script — you'll hear a welcome message.
2. When asked if you want to do calculations, type `yes` or `no`.
3. Enter a mathematical expression when prompted.

   ```
   Example inputs:
     2 + 3
     10 * (4 - 2)
     100 / 5 + 3 ** 2
   ```

4. After each result, you'll be asked if you want to **continue**.
   - Type `yes` — enter another expression to append and continue.
   - Type `no` — the program will thank you and exit.

---

## 🗂️ Code Overview

| Function | Description |
|---|---|
| `speak(text)` | Converts a string to speech and prints it |
| `speak1(emoji, text)` | Like `speak()`, but also prints an emoji prefix |
| `see(m)` | Asks the user to continue or stop; chains expressions |
| `calculator(s)` | Evaluates the expression and loops for further input |
| `main()` | Entry point — greets user and starts the calculator |

### Flow Diagram

```
main()
  └─ User says "yes"
       └─ Enter expression
            └─ calculator(s)
                 ├─ Evaluates expression
                 ├─ Speaks result
                 └─ see(v)
                      ├─ "yes" → append new expression → back to calculator
                      └─ "no"  → exit
```

---


## ⚠️ Known Limitations

- Requires a working audio output device for speech to function.
- Voice index `voices[1]` assumes a female/secondary voice is available — may vary by OS.
- The `see()` function uses recursion for invalid answers, which could stack overflow on repeated bad input.

---


## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- [`pyttsx3`](https://pypi.org/project/pyttsx3/) for offline text-to-speech
- Python's `ast` module (used internally by `simpleeval`) for safe expression parsing

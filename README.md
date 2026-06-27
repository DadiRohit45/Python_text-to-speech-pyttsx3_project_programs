# 🔊 pyttsx3 Mini Projects

A collection of mini projects built using **Python and pyttsx3** — a text-to-speech library that works completely offline. Each project is self-contained in its own folder with its own code and documentation.

---

## 📋 Table of Contents

- [About pyttsx3](#about-pyttsx3)
- [Projects](#projects)
- [Requirements](#requirements)
- [How to Run Any Project](#how-to-run-any-project)
- [Repository Structure](#repository-structure)
- [Author](#author)

---

## 🔊 About pyttsx3

`pyttsx3` is a Python text-to-speech conversion library that works **offline** — no internet connection needed. It supports multiple voices, adjustable speech rate, and volume control, making it perfect for building voice-enabled desktop applications.

```python
import pyttsx3
engine = pyttsx3.init()
engine.say("Hello, I can speak!")
engine.runAndWait()
```

---

<!-- PROJECTS_START -->
## 🗂️ Projects

| Project | Description | Key Libraries |
|---|---|---|
| [🧮 Talking Calculator](./Talking_calculator/README.md) | A Python-based interactive calculator with **text-to-speech** support, allowing users to perform mathematical calculations through voice feedback and text input. | `pyttsx3`, `simpleeval` |

<!-- PROJECTS_END -->

---

<!-- REQUIREMENTS_START -->
## 🛠️ Requirements

- Python 3.6+

**Install via pip:**
- [`pyttsx3`](https://pypi.org/project/pyttsx3/) — offline text-to-speech engine
- [`simpleeval`](https://pypi.org/project/simpleeval/) — safe math expression evaluator

Install all at once:
```bash
pip install pyttsx3 simpleeval
```

<!-- REQUIREMENTS_END -->
---

## 🚀 How to Run Any Project

1. Navigate into the project folder:
   ```bash
   cd voice-calculator
   ```

2. Run the Python file:
   ```bash
   python calculator.py
   ```

---
<!-- STRUCTURE_START -->
## 📁 Repository Structure

```text
Python_text-to-speech-pyttsx3_project_programs/
│
├── README.md                          ← You are here (parent README)
│
└── Talking_calculator/
    ├── README.md  ← Talking Calculator documentation
    └── Talking_Calculator.py  ← Talking Calculator source code
```

<!-- STRUCTURE_END -->
---

## 👤 Author

- **Dadi Rohit** — [DadiRohit45](https://github.com/DadiRohit45)

---

## 📄 License

This repository is open-source and available under the [MIT License](LICENSE).

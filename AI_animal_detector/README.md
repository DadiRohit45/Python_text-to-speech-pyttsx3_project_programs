# 🐾 AI Animal Guessing Game

A fun, voice-interactive Python application that guesses an animal based on your answers to simple yes/no questions — with text-to-speech narration powered by `pyttsx3`.

---

## 📋 Features

- Voice-guided interaction using a female TTS voice
- Emoji-enhanced console output for a lively experience
- Identifies animals based on 4 characteristics:
  - **Legs** — does it have 4 legs?
  - **Swimming** — can it swim?
  - **Barking** — does it bark?
  - **Pet** — is it a pet animal?

---

## 🛠️ Requirements

- Python 3.x
- `pyttsx3` library

### Install Dependencies

```bash
pip install pyttsx3
```

> **Note:** `pyttsx3` may require additional system dependencies depending on your OS:
> - **Windows:** No extra setup needed (uses SAPI5)
> - **macOS:** No extra setup needed (uses `nsss`)
> - **Linux:** Install `espeak` via `sudo apt install espeak`

> **Voice Note:** The app uses `voices[1]` (typically a female voice). If you get an error, your system may only have one voice installed. Change `voices[1].id` to `voices[0].id` as a fallback.

---

## 🚀 How to Run

```bash
python animal_guesser.py
```

---

## 🎮 Usage

Answer each question with **`yes`** or **`no`** when prompted:

| Question | Input |
|----------|-------|
| Does the animal have 4 legs? | `yes` / `no` |
| Does the animal swim? | `yes` / `no` |
| Does the animal bark? | `yes` / `no` |
| Is it a pet animal? | `yes` / `no` |

---

## 🧠 Guessing Logic

| Legs | Swims | Barks | Pet | Guess |
|------|-------|-------|-----|-------|
| yes | yes | yes | yes | 🐕 Dog |
| yes | no | no | yes | 🐈 Cat |
| yes | no | yes | no | 🦁 Lion |
| yes | yes | yes | no | 🐅 Tiger |
| no | yes | no | yes | 🐬 Fish |
| no | yes | no | no | Human |
| any other combination | — | ❓ Unknown Animal |

---

## 📁 Project Structure

```
animal_guesser/
│
└── animal_guesser.py    # Main application file
```

---



---

## 👨‍💻 Author

Built as a beginner-friendly Python + TTS project exploring voice interaction and rule-based logic through a fun animal guessing game.

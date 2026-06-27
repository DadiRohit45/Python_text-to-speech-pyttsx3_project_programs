# 🎬 AI Cartoon Recommender

A voice-interactive Python application that recommends cartoons based on your age, mood, and preferred cartoon genre — with text-to-speech powered by `pyttsx3`.

---

## 📋 Features

- Voice-guided interaction using text-to-speech
- Personalized cartoon recommendations based on:
  - **Age**
  - **Mood** (happy, sad, bored, excited)
  - **Cartoon type preference** (action, funny, adventure)

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

---

## 🚀 How to Run

```bash
python cartoon_recommender.py
```

---

## 🎮 Usage

Once launched, the program will speak and prompt you for the following inputs:

| Prompt | Expected Input |
|--------|----------------|
| Your age | A number (e.g., `20`) |
| Your mood | `happy`, `sad`, `bored`, or `excited` |
| Cartoon type you like | `action`, `funny`, or `adventure` |

---

## 🎯 Recommendation Logic

| Age | Mood | Type | Recommendation |
|-----|------|------|----------------|
| Under 18 | happy | action | Jackie Chan Adventures |
| Under 18 | sad | funny | Shinchan |
| Under 18 | bored | adventure | Doraemon |
| 18+ | any | any | Recommends Anime |

---

## 📁 Project Structure

```
cartoon_recommender/
│
└── cartoon_recommender.py   # Main application file
```

---



---



---

## 👨‍💻 Author

Built as a beginner-friendly Python + TTS project to explore voice interaction and rule-based recommendation systems.

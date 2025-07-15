# 🧠 Reddit Persona Generator

This Python script scrapes a Reddit user's posts and comments, analyzes them using an LLM (via OpenRouter), and generates a detailed **user persona** with **citations** to the original content.

It was created as part of a hiring assignment for the position of **AI/LLM Engineer Intern at BeyondChats**.

---

## 🚀 Features

- 🔍 Scrapes all **posts** and **comments** from a Reddit user
- 🤖 Uses an **LLM (Mistral-7B)** to infer:
  - Age range
  - Interests
  - Personality traits
  - Writing style
  - Political/social views
  - Frequent subreddits
- 📎 Cites original Reddit URLs as evidence
- 📂 Saves the generated persona to a `.txt` file

---

## 🛠️ Tech Stack

- Python 3
- [`praw`](https://praw.readthedocs.io/) – Reddit API wrapper
- [`openai`](https://github.com/openai/openai-python) – for calling OpenRouter-compatible LLMs
- [`dotenv`](https://pypi.org/project/python-dotenv/) – manages API keys
- [`tqdm`](https://github.com/tqdm/tqdm) – progress bar utility
- [OpenRouter](https://openrouter.ai) – LLM backend using `mistralai/mistral-7b-instruct`

---

## 📁 Project Structure

reddit-persona-generator/
│
├── generate_persona.py
├── requirements.txt
├── .env
├── outputs/
│   ├── kojied_persona.txt
│   └── hungry-move-6603_persona.txt
├── README.md
└── utils/
    └── reddit_scraper.py

## 🔐 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/reddit-persona-generator.git
cd reddit-persona-generator

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Configure Environment Variables
Rename .env.example to .env and fill in your credentials:
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_secret
REDDIT_USER_AGENT=script:reddit.persona:v1.0 (by /u/your_reddit_username)

OPENROUTER_API_KEY=sk-or-...

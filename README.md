
# Movie Genre Recommender (Chatbot Interface)
This is an interactive quick chatbot prototype to test [Gradio](https://gradio.app/) and the OpenAI API. It simulates a friendly movie expert that asks you a series of Yes/No questions and recommends up to 3 movie genres based on your preferences. 

## What It Does
- Uses GPT (default: `gpt-3.5-turbo`) to drive a guided conversation.
- Asks 10 Yes/No questions related to movie preferences.
- Only accepts "yes" or "no" — rejects and re-prompts otherwise.
- Recommends 3 movie genres at the end.
  
## Setup Instructions
### 1. Clone the repo
```bash
git  clone  https://github.com/apadin-repo/movie-chatbot.git
cd  movie-chatbot
```

### 2. Create and activate a virtual environment
```bash
python  -m  venv  .venv
source  .venv/bin/activate  # macOS/Linux
# OR
.venv\Scripts\activate  # windows
```

### 3. Install dependencies
```bash
pip  install  -r  requirements.txt
```

### 4. Create a `.env` file
Create a `.env` file in the project root:
```env
OPENAI_API_KEY=<your-key>
```

## Run the App
From the project root, run:
```bash
python  app.py
```
Once running, you’ll see:

```
Running on local URL: http://127.0.0.1:7860
```
Open that URL in your browser.
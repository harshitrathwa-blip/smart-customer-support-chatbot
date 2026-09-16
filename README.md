# Smart Customer Support Chatbot

An intelligent customer support chatbot built for **SmartMart** using **Natural Language Processing (NLP)** and **Generative AI**, powered by Google's **Gemini 2.5 Flash**.

---

## Features
- **Interactive Chat Interface**: Built natively using Streamlit chat elements.
- **Lightweight NLP Layer**: Rule-based intent detection and keyword extraction with an educational **NLP Analysis** expander.
- **Context-Aware Memory**: Multi-turn session state tracking enabling smooth follow-up conversations.
- **SmartMart Business Context**: Strict system prompts enforcing accurate representation of fictional company policies.
- **Robust Error Handling**: Handles missing configuration keys, rate limits, and network errors gracefully.

---

## Technology Stack
- **Language**: Python 3.10+
- **Frontend UI**: Streamlit
- **LLM**: Google Gemini 2.5 Flash (`google-genai` SDK)
- **Utilities**: python-dotenv, pandas

---

## Project Structure
```text
smart-customer-support-chatbot/
│
├── app.py                  # Streamlit user interface & layout
├── chatbot.py              # Gemini client initialization & system prompt handling
├── nlp_utils.py            # Text preprocessing & rule-based intent parsing
├── config.py               # Secure environment & secrets loader
├── requirements.txt        # Project dependencies
├── .env.example            # Environment variable template
├── .gitignore              # Git ignore rules
├── README.md               # Project documentation
└── AGENTS.md               # Developer instructions
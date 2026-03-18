# CodeAlpha FAQ Chatbot

A lightweight FAQ chatbot built with **Streamlit** + **scikit-learn** that matches user questions to a small FAQ list using **TF-IDF + cosine similarity**.

## 🚀 Features

- Natural language question input
- Matches questions to stored FAQ items
- Shows relevant answer if similarity is sufficient
- Streamlit UI for easy interaction

## 📦 Project Structure

- `app.py` – Streamlit frontend
- `chatbot/chatbot.py` – TF-IDF matching logic
- `chatbot/faqs.py` – FAQ data store

## ⚙️ Requirements

- Python 3.9+ (or compatible)
- `streamlit`
- `scikit-learn`

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the app

From the project root:

```bash
streamlit run app.py
```

Then open the URL shown in your terminal (usually `http://localhost:8501`).

## 🛠️ Customizing FAQs

Edit `chatbot/faqs.py` to add, remove, or update question/answer pairs.

## 📌 Notes

- The bot returns a default fallback message when no FAQ item is sufficiently similar.
- This is a lightweight demo and not designed for production-grade conversational AI.

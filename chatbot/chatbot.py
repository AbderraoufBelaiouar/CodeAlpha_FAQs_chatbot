import re

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .faqs import faq_list

for pkg in ("punkt", "wordnet", "omw-1.4", "stopwords"):
    try:
        nltk.data.find(f"tokenizers/{pkg}" if pkg == "punkt" else f"corpora/{pkg}")
    except LookupError:
        nltk.download(pkg)

lemmatizer = WordNetLemmatizer()
_stopwords = set(stopwords.words("english"))


def preprocess(text: str) -> str:
    """Normalize, tokenize, remove stopwords, and lemmatize a text string."""
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    tokens = nltk.word_tokenize(text)
    tokens = [t for t in tokens if t.isalpha() and t not in _stopwords]
    lemmas = [lemmatizer.lemmatize(t) for t in tokens]
    return " ".join(lemmas)


list_of_sentences = [faq["question"] for faq in faq_list]
processed_sentences = [preprocess(s) for s in list_of_sentences]


def compute_most_similar(sentence1):
    sentence1 = preprocess(sentence1)
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([sentence1] + processed_sentences)

    similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])

    scores = similarity_matrix[0]
    return scores


def get_question_answer(sentence):
    scores = compute_most_similar(sentence)
    max_index = scores.argmax()
    if scores[max_index] > 0.1:
        return faq_list[max_index]["answer"]
    else:
        return "Sorry, I don't have an answer for that question."

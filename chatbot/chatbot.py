from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .faqs import faq_list
list_of_sentences = [faq['question'] for faq in faq_list]
def compute_most_similar(sentence1):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([sentence1] + list_of_sentences)

    similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])

    scores = similarity_matrix[0]
    return scores
def get_question_answer(sentence):
    scores = compute_most_similar(sentence)
    max_index = scores.argmax()
    if scores[max_index] > 0.1:  
        return faq_list[max_index]['answer']
    else:
        return "Sorry, I don't have an answer for that question."

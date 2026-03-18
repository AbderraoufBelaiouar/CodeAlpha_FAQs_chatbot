import streamlit as st

from chatbot.chatbot import get_question_answer
from chatbot.faqs import faq_list

st.set_page_config(page_title="CodeAlpha FAQ Chatbot", layout="centered")

st.title("🧠 CodeAlpha FAQ Chatbot")
st.write("Ask a question and I'll try to find the best match from the FAQ list.")

if "history" not in st.session_state:
    st.session_state.history = []

if "show_faqs" not in st.session_state:
    st.session_state.show_faqs = True

# Ensure we can clear the input field after submitting
if st.session_state.get("clear_input", False):
    st.session_state.user_input = ""
    st.session_state.clear_input = False

with st.form("chat_form"):
    user_input = st.text_input("Your question", key="user_input", placeholder="Type your question here...")
    submitted = st.form_submit_button("Ask")

    if submitted and user_input:
        answer = get_question_answer(user_input)
        st.session_state.history.append({"question": user_input, "answer": answer})
        st.session_state.clear_input = True

if st.session_state.history:
    st.write("---")
    st.write("### Conversation")
    for entry in st.session_state.history:
        st.markdown(f"**You:** {entry['question']}")
        st.markdown(f"**Bot:** {entry['answer']}")
        st.write("\n")

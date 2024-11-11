import streamlit as st
from transformers import pipeline

# Set up the question-answering pipeline
@st.cache_resource
def load_qa_pipeline():
    return pipeline("question-answering")

qa_pipeline = load_qa_pipeline()

# Streamlit app layout
st.title("Question Answering App")
st.write("Paste text into the document box, ask a question, and get an answer based on the document.")

# Document input box
document_text = st.text_area("Document Text", height=200)

# Question input box
question_text = st.text_input("Ask a question")

# Generate answer when button is clicked
if st.button("Get Answer"):
    if document_text and question_text:
        with st.spinner("Finding the answer..."):
            result = qa_pipeline(question=question_text, context=document_text)
            answer = result["answer"]
            st.subheader("Answer")
            st.write(answer)
    else:
        st.warning("Please provide both document text and a question.")

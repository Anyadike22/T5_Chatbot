import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from langchain_groq.chat_models import ChatGroq
import os

# Initialize the language model
llm = ChatGroq(
    model_name="llama2-70b-4096",  # Verify this is the correct model name
    api_key=st.secrets["GROQ_API_KEY"]  # Use Streamlit secrets
)

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("Africa Infrastructure Development Index AIDI.csv")

df = load_data()
smart_df = SmartDataframe(df, config={"llm": llm})

# Initialize session state for question history
if 'question_history' not in st.session_state:
    st.session_state.question_history = []

# Streamlit interface
st.title("Exploring Conversations with Data using LLM")

# Display data
st.sidebar.header("Options")
show_data = st.sidebar.checkbox("Show raw data")
if show_data:
    st.subheader("AIDI Data")
    st.dataframe(df.head(20))

user_question = st.text_input("Ask a question about the data.")

# Display the response to the user's question
if st.button("Get Answer"):
    answer = smart_df.chat(user_question)
    st.write(answer)
    st.session_state.question_history.append(user_question)
    
    # Check if a chart was generated
    if hasattr(smart_df, 'last_code_execution'):
        if smart_df.last_code_execution.output:
            st.pyplot(smart_df.last_code_execution.output)

# Display the history of questions
st.subheader("Question History")
for i, question in enumerate(st.session_state.question_history, 1):
    st.write(f"{i}. {question}")

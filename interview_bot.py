import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

# -------------------------
# API KEY
# -------------------------
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# -------------------------
# LLM (BETTER MODEL)
# -------------------------
llm = ChatGroq(
    temperature=0.7,
    model_name="llama-3.3-70b-versatile"
)

# -------------------------
# PROMPT
# -------------------------
prompt = PromptTemplate.from_template(
"""
You are an HR interviewer from a top product based company 
(Google, Amazon, Microsoft, Meta).

Your job:
1. Conduct a realistic HR interview
2. Ask one question at a time
3. After candidate answers, give short feedback
4. Ask the next question

Conversation History:
{history}

Candidate Answer:
{answer}

Respond like a professional HR interviewer.
"""
)

chain = prompt | llm

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="AI HR Interview Simulator",
    page_icon="💼",
    layout="centered"
)

st.title("💼 AI HR Interview Simulator")
st.write("Practice HR interviews like product based companies")

# -------------------------
# SESSION STATE
# -------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "started" not in st.session_state:
    st.session_state.started = False

# -------------------------
# START BUTTON
# -------------------------
if not st.session_state.started:

    if st.button("Start Interview"):

        st.session_state.started = True

        first_q = "Welcome to the interview. Let's begin.\n\nTell me about yourself."

        st.session_state.messages.append({
            "role": "assistant",
            "content": first_q
        })

# -------------------------
# DISPLAY CHAT
# -------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

# -------------------------
# USER INPUT
# -------------------------
if st.session_state.started:

    user_input = st.chat_input("Type your answer...")

    if user_input:

        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        with st.chat_message("user"):
            st.write(user_input)

        history_text = "\n".join(
            [m["role"] + ": " + m["content"] for m in st.session_state.messages]
        )

        response = chain.invoke({
            "history": history_text,
            "answer": user_input
        })

        bot_reply = response.content

        st.session_state.messages.append({
            "role": "assistant",
            "content": bot_reply
        })

        with st.chat_message("assistant"):
            st.write(bot_reply)
AI Interviewer Bot is an AI-powered HR interview chatbot that simulates realistic job interviews from top product-based companies like Google, Amazon, Microsoft, and Meta. Built with Streamlit and powered by Groq's LLaMA 3.3 70B model via LangChain.

**Prequisites:**
Get an API Key from any of the AI chatbots. (Get your free Groq API key at: https://console.groq.com)

**Methodology:**
The application follows a conversational AI pipeline:
1. User triggers the interview by clicking "Start Interview".
2. The bot greets the user and asks the first question: "Tell me about yourself."
3. The user types their answer in the chat input.
4. The full conversation history is passed along with the new answer to the LLM prompt.
5. The LLM (LLaMA 3.3 70B via Groq) responds as a professional HR interviewer — gives feedback and     asks the next question.
6. This loop continues, maintaining context across the entire session using Streamlit session state.

**Components Used:**
streamlit                                Frontend UI — chat interface, session state, page config
langchain_groq                           LangChain integration with Groq's API
langchain_core.prompts.PromptTemplate    Builds the structured prompt with conversation history
Groq API                                 Cloud inference provider for the LLaMA model
llama-3.3-70b-versatile                  The underlying LLM that powers the interviewer
os                                       Used to set the Groq API key as an environment variable

**How to Run:**
1. Clone the Repository
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME
2. Create a Virtual Environment (Recommended)
    python -m venv venv
    venv\Scripts\activate
3. Install Dependencies
   pip install streamlit langchain-groq langchain-core
4. Set Your Groq API Key
   ⚠️ Important: Never hardcode your API key in the source code. Use a .env file or environment variable instead.
5. Run the App
   streamlit run interview_bot.py

**Requirements:**
    > streamlit
    > langchain-groq
    > langchain-core


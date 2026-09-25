from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="MediBot AI",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

body {
    background-color: #f8fafc;
}

.main {
    background-color: #f8fafc;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #0f172a;
    margin-top: 10px;
}

.subtitle {
    text-align: center;
    font-size: 17px;
    color: #64748b;
    margin-bottom: 30px;
}

.welcome {
    background-color: white;
    padding: 30px;
    border-radius: 20px;
    border: 1px solid #e2e8f0;
    margin-bottom: 25px;
}

.welcome h2 {
    color: #0f172a;
}

.welcome p {
    color: #64748b;
    font-size: 16px;
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #e2e8f0;
    height: 150px;
}

.card h3 {
    color: #0f172a;
}

.card p {
    color: #64748b;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# VECTOR DATABASE
# =========================================================

DB_FAISS_PATH = "vectorstore/db_faiss"


@st.cache_resource
def load_vectorstore():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.load_local(
        DB_FAISS_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vectorstore


# =========================================================
# PROMPT
# =========================================================

CUSTOM_PROMPT = """
Use the following context to answer the user's question.

Rules:

1. Only use information from the provided context.
2. Do not make up information.
3. If the answer is not available in the context, say:
   "I don't have enough information in my medical knowledge base to answer that."
4. Give a clear and simple answer.
5. Do not diagnose the user.
6. Do not replace professional medical advice.

Context:
{context}

Question:
{question}

Answer:
"""


def create_prompt():

    return PromptTemplate(
        template=CUSTOM_PROMPT,
        input_variables=[
            "context",
            "question"
        ]
    )


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("🩺 MediBot AI")

    st.write(
        "Your AI-powered medical information assistant."
    )

    st.divider()

    st.subheader("💡 You can ask about")

    st.write("🩸 Symptoms and diseases")
    st.write("❤️ Medical conditions")
    st.write("💊 General health information")
    st.write("🔬 Causes and risk factors")
    st.write("🛡️ Prevention")
    st.write("📚 Treatment information")

    st.divider()

    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()

    st.warning(
        "⚠️ Medical Disclaimer\n\n"
        "MediBot provides general medical information "
        "for educational purposes only. It is not a "
        "replacement for a qualified healthcare professional."
    )


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="title">🩺 MediBot AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Intelligent Medical Information Assistant'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# API KEY
# =========================================================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:

    st.error(
        "GROQ_API_KEY is missing."
    )

    st.info(
        "Make sure your .env file contains:\n\n"
        "GROQ_API_KEY=your_api_key"
    )

    st.stop()


# =========================================================
# SESSION STATE
# =========================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# =========================================================
# WELCOME SCREEN
# =========================================================

if len(st.session_state.messages) == 0:

    st.markdown(
        """
        <div class="welcome">

        <h2>👋 Welcome to MediBot</h2>

        <p>
        Ask me a medical question and I will search
        my medical knowledge base to provide a
        context-based answer.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("💬 Try asking")


    # -----------------------------------------------------
    # QUESTION BUTTONS
    # -----------------------------------------------------

    col1, col2, col3 = st.columns(3)


    with col1:

        if st.button(
            "🩸 What is diabetes?",
            use_container_width=True
        ):

            st.session_state.selected_question = (
                "What is diabetes?"
            )

            st.rerun()


    with col2:

        if st.button(
            "❤️ What is hypertension?",
            use_container_width=True
        ):

            st.session_state.selected_question = (
                "What is hypertension?"
            )

            st.rerun()


    with col3:

        if st.button(
            "🫁 What are asthma symptoms?",
            use_container_width=True
        ):

            st.session_state.selected_question = (
                "What are the symptoms of asthma?"
            )

            st.rerun()


    st.write("")


    # -----------------------------------------------------
    # FEATURE CARDS
    # -----------------------------------------------------

    col1, col2, col3 = st.columns(3)


    with col1:

        st.markdown(
            """
            <div class="card">

            <h3>🧠 AI Powered</h3>

            <p>
            Uses an AI language model to understand
            medical questions.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
            """
            <div class="card">

            <h3>📚 RAG Based</h3>

            <p>
            Retrieves relevant information from
            the medical knowledge base.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col3:

        st.markdown(
            """
            <div class="card">

            <h3>⚡ Fast</h3>

            <p>
            Uses Groq for fast AI inference and
            responsive answers.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# CHAT HISTORY
# =========================================================

for message in st.session_state.messages:

    if message["role"] == "user":

        with st.chat_message(
            "user",
            avatar="🧑"
        ):

            st.markdown(
                message["content"]
            )

    else:

        with st.chat_message(
            "assistant",
            avatar="🩺"
        ):

            st.markdown(
                message["content"]
            )


# =========================================================
# USER INPUT
# =========================================================

user_question = st.chat_input(
    "Ask MediBot a medical question..."
)


# =========================================================
# SUGGESTED QUESTION
# =========================================================

if "selected_question" in st.session_state:

    user_question = st.session_state.selected_question

    del st.session_state.selected_question


# =========================================================
# PROCESS QUESTION
# =========================================================

if user_question:

    # -----------------------------------------------------
    # SHOW USER MESSAGE
    # -----------------------------------------------------

    with st.chat_message(
        "user",
        avatar="🧑"
    ):

        st.markdown(
            user_question
        )


    # Save user message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )


    try:

        # -------------------------------------------------
        # LOAD VECTOR DATABASE
        # -------------------------------------------------

        with st.spinner(
            "📚 Loading medical knowledge base..."
        ):

            vectorstore = load_vectorstore()


        # -------------------------------------------------
        # CREATE LLM
        # -------------------------------------------------

        llm = ChatGroq(
            model_name="openai/gpt-oss-120b",
            temperature=0,
            groq_api_key=GROQ_API_KEY
        )


        # -------------------------------------------------
        # CREATE RAG CHAIN
        # -------------------------------------------------

        qa_chain = RetrievalQA.from_chain_type(

            llm=llm,

            chain_type="stuff",

            retriever=vectorstore.as_retriever(
                search_kwargs={
                    "k": 3
                }
            ),

            return_source_documents=True,

            chain_type_kwargs={
                "prompt": create_prompt()
            }
        )


        # -------------------------------------------------
        # GET RESPONSE
        # -------------------------------------------------

        with st.chat_message(
            "assistant",
            avatar="🩺"
        ):

            with st.spinner(
                "🔎 Searching medical knowledge..."
            ):

                response = qa_chain.invoke(
                    {
                        "query": user_question
                    }
                )


            answer = response["result"]

            source_documents = response[
                "source_documents"
            ]


            # -------------------------------------------------
            # SHOW ANSWER
            # -------------------------------------------------

            st.markdown(answer)


            # -------------------------------------------------
            # SHOW SOURCES
            # -------------------------------------------------

            if source_documents:

                with st.expander(
                    "📚 View Retrieved Sources"
                ):

                    for index, document in enumerate(
                        source_documents
                    ):

                        st.markdown(
                            f"### 📄 Source {index + 1}"
                        )

                        st.write(
                            document.page_content
                        )

                        st.divider()


        # -------------------------------------------------
        # SAVE ANSWER
        # -------------------------------------------------

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )


    except Exception as error:

        st.error(
            f"❌ Error: {str(error)}"
        )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "🩺 MediBot AI • RAG-powered Medical Assistant"
)
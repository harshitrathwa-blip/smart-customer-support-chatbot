import streamlit as st
from chatbot import generate_chatbot_response
from nlp_utils import detect_intent
from config import get_gemini_api_key

# Page Configuration
st.set_page_config(
    page_title="Smart Customer Support Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Initialize Session State for chat messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! Welcome to SmartMart Customer Support. How can I assist you today?"}
    ]

# Sidebar Configuration
with st.sidebar:
    st.image("https://img.icons8.com/color/96/chatbot.png", width=70)
    st.markdown("### About SmartMart")
    st.markdown(
        "This is an intelligent, NLP-powered customer support chatbot representing **SmartMart** "
        "built with Streamlit and **Gemini 2.5 Flash**."
    )
    
    st.markdown("---")
    st.markdown("### How to Use")
    st.markdown("1. Type your question in the chat bar below.\n2. Click suggested questions for quick assistance.\n3. Expand **NLP Analysis** to review intent detection.")
    
    st.markdown("---")
    st.markdown("### Supported Topics")
    st.markdown(
        "- Business Hours\n- Order Tracking & Status\n- Returns & Refunds\n- Payment Issues\n- Delivery Policies"
    )
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Clear Chat", use_container_width=True):
            st.session_state.messages = [
                {"role": "assistant", "content": "Chat history cleared. How can I help you with SmartMart today?"}
            ]
            st.rerun()
    with col2:
        if st.button("New Session", use_container_width=True):
            st.session_state.messages = [
                {"role": "assistant", "content": "Started a new conversation session. Welcome back to SmartMart support!"}
            ]
            st.rerun()

# Main Title Area
st.title("🤖 Smart Customer Support Chatbot")
st.markdown("*An NLP + Generative AI customer support assistant powered by Gemini 2.5 Flash*")
st.markdown("<small><b>Technologies:</b> Python | NLP | Gemini 2.5 Flash | Streamlit</small>", unsafe_allow_html=True)
st.markdown("---")

# Check API Key validity upfront
api_key = get_gemini_api_key()
if not api_key:
    st.error("⚠️ Gemini API key is not configured. Please add `GEMINI_API_KEY` to your `.env` file or Streamlit Secrets.")
    st.stop()

# Display chat history using native Streamlit chat components
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Suggested Prompt Cards / Buttons
st.markdown("##### Quick Suggestions:")
s_col1, s_col2, s_col3, s_col4 = st.columns(4)
suggested_query = None

with s_col1:
    if st.button("Track my order?"):
        suggested_query = "How can I track my order?"
with s_col2:
    if st.button("Return policy?"):
        suggested_query = "What is your return policy?"
with s_col3:
    if st.button("Accepted payments?"):
        suggested_query = "What payment methods do you accept?"
with s_col4:
    if st.button("Delivery time?"):
        suggested_query = "How long does delivery take?"

# Accept user input via chat input or suggested button click
user_input = st.chat_input("Ask your question about SmartMart...")
if suggested_query:
    user_input = suggested_query

if user_input:
    # Append user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Perform lightweight NLP Intent Detection
    intent, keywords = detect_intent(user_input)

    # Display optional educational NLP Analysis expander
    with st.expander("🔍 NLP Analysis (Educational View)", expanded=False):
        st.write(f"**Detected Intent:** `{intent}`")
        st.write(f"**Extracted Keywords:** `{keywords if keywords else 'None'}`")

    # Generate response from Gemini 2.5 Flash with loading spinner
    with st.chat_message("assistant"):
        with st.spinner("SmartMart support is typing..."):
            try:
                response_text = generate_chatbot_response(st.session_state.messages)
                st.markdown(response_text)
                # Append assistant response to history
                st.session_state.messages.append({"role": "assistant", "content": response_text})
            except Exception as e:
                error_msg = "An error occurred while connecting to Gemini service. Please check your network or API key configuration."
                st.error(f"{error_msg}")
                st.exception(e)  # TEMPORARY - shows real error, remove before final submission

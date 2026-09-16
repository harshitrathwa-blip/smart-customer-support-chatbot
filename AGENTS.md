# AGENTS.md - Project Development Instructions

- Implement using Python-only standards.
- Build UI exclusively using Streamlit components (`st.chat_message`, `st.chat_input`, `st.spinner`, etc.).
- Utilize Gemini 2.5 Flash (`gemini-2.5-flash`) via the modern `google-genai` package.
- Never hardcode API keys under any circumstances.
- Keep module structure clean, modular, and separated into config, nlp_utils, chatbot, and app.
- Use clear variable names and robust error handling blocks.
- Avoid introducing unnecessary or bloated dependencies.
- Ensure full compatibility with Streamlit Community Cloud deployment guidelines.
- Never modify `.env.example` file structures unnecessarily.
- Test app startup and runtime pathways before marking complete.
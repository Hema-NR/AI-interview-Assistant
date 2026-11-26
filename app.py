
import streamlit as st
from groq import Groq
from streamlit.errors import StreamlitSecretNotFoundError

st.set_page_config(
    page_title="AI Interview Assistant",
    layout="centered"
)

st.title("AI Interview Assistant")

st.caption(
    "Practice interviews with AI-generated questions and constructive feedback."
)

st.caption("Launched by: HEMA NR")
st.write("Department of AI & DS")

# API connection
try:
    api_key = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=api_key)

except (KeyError, FileNotFoundError, StreamlitSecretNotFoundError):
    st.error(
        "GROQ_API_KEY is missing. "
        "Add it to your Streamlit secrets."
    )
    st.stop()

# Select job role
role = st.selectbox(
    "Select Job Role",
    [
        "Python Developer",
        "Java Developer",
        "Data Analyst",
        "Machine Learning Engineer",
        "Software Engineer",
        "HR Executive"
    ]
)

# Generate interview questions
if st.button("Generate Interview Questions"):

    prompt = f"Generate 5 interview questions for the role of {role}."

    try:
        with st.spinner("Generating interview questions..."):

            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert technical interviewer. Generate clear and relevant interview questions."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            output = response.choices[0].message.content

            st.subheader("Interview Questions")
            st.write(output)

    except Exception as e:
        st.error(f"Error generating questions: {e}")

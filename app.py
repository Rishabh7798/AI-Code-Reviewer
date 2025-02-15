import streamlit as st
import google.generativeai as genai
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.let_it_rain import rain

API_KEY = "AIzaSyDuLiCCvqZeHk9r0uxp-9ESdlwICyyR90U"
genai.configure(api_key=API_KEY)

def review_code(user_code):
    try:
        model = genai.GenerativeModel("gemini-pro")  
        prompt = f"""
        Review the following Python code and provide feedback on potential bugs, improvements, and best practices.
        Also, suggest a corrected version if needed.
        
        Code:
        ```python
        {user_code}
        ```
        """
        response = model.generate_content(prompt)  
        return response.text  
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Custom UI Styling
st.set_page_config(page_title="AI Code Reviewer", page_icon="🤖", layout="wide")
st.markdown("""
    <style>
        .title-text {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #4CAF50;
        }
        .sub-text {
            text-align: center;
            font-size: 18px;
            color: #777;
        }
        .stTextArea textarea {
            font-size: 16px;
            font-family: 'Courier New', monospace;
            background-color: #303030 !important; /* Dark Gray Background */
            color: white !important; /* White Text */
        }
        .review-box {
            background-color: #303030 !important; /* Dark Gray Background */
            color: white !important; /* White Text */
            padding: 15px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title-text'>🤖AI Code Reviewer (GenAI)🤖</h1>", unsafe_allow_html=True)
st.markdown("<h4 class='sub-text'>🔎Analyze your Python code with AI🔍</h4>", unsafe_allow_html=True)
add_vertical_space(2)

user_code = st.text_area("✨Paste your Python code below:", height=300)

if st.button("🚀 Review Code 🚀", use_container_width=True):
    if user_code.strip():
        with st.spinner("🤖 Analyzing your code..."):
            review_result = review_code(user_code)
        
        # Display Result
        st.subheader("📊 AI Code Review:")
        st.markdown(f"<div class='review-box'>{review_result}</div>", unsafe_allow_html=True)
    else:
        st.warning("⚠️Please enter some Python code to review.⚠️")

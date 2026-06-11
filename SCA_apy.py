# ===============================
# Smart Cybersecurity Assistant 🛡️
# Powered by Google Gemini API
# ===============================

import streamlit as st
import google.generativeai as genai

# ===============================
# CONFIGURE API KEY
# ===============================

genai.configure(api_key="Gemini API")

model = genai.GenerativeModel("gemini-3-flash-preview")

# ===============================
# FUNCTIONS
# ===============================

def analyze_phishing(email_text):
    prompt = f"""
You are a cybersecurity expert.

Analyze the following email and determine whether it is a phishing attempt.

Provide:
- Risk level (Low / Medium / High)
- Explanation
- Suspicious indicators

Email:
{email_text}
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error: {e}"


def analyze_code(code):
    prompt = f"""
You are a cybersecurity expert.

Analyze the following code for security vulnerabilities.

Provide:
- Vulnerabilities found
- Risk level
- Fix suggestions

Code:
{code}
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error: {e}"


def password_checker(password):
    prompt = f"""
Evaluate the strength of this password.

Provide:
- Score (1-10)
- Weaknesses
- Suggestions

Password:
{password}
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error: {e}"


# ===============================
# STREAMLIT UI
# ===============================

st.set_page_config(
    page_title="Cybersecurity Assistant",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ Smart Cybersecurity Assistant")
st.write("AI-powered cybersecurity analysis using Google Gemini")

# ===============================
# SIDEBAR
# ===============================

option = st.sidebar.selectbox(
    "Choose Tool",
    [
        "Phishing Detector",
        "Code Security Analyzer",
        "Password Checker"
    ]
)

# ===============================
# PHISHING DETECTOR
# ===============================

if option == "Phishing Detector":

    st.header("📧 Phishing Email Detector")

    email_input = st.text_area(
        "Paste suspicious email content"
    )

    if st.button("Analyze Email"):

        if email_input.strip() == "":
            st.warning("Please enter email content")

        else:
            with st.spinner("Analyzing email..."):
                result = analyze_phishing(email_input)

            st.success("Analysis Complete")
            st.write(result)

# ===============================
# CODE ANALYZER
# ===============================

elif option == "Code Security Analyzer":

    st.header("💻 Code Vulnerability Scanner")

    code_input = st.text_area(
        "Paste your code here"
    )

    if st.button("Analyze Code"):

        if code_input.strip() == "":
            st.warning("Please enter code")

        else:
            with st.spinner("Scanning code..."):
                result = analyze_code(code_input)

            st.success("Analysis Complete")
            st.write(result)

# ===============================
# PASSWORD CHECKER
# ===============================

elif option == "Password Checker":

    st.header("🔑 Password Strength Checker")

    password_input = st.text_input(
        "Enter password",
        type="password"
    )

    if st.button("Check Password"):

        if password_input.strip() == "":
            st.warning("Please enter a password")

        else:
            with st.spinner("Checking password..."):
                result = password_checker(password_input)

            st.success("Analysis Complete")
            st.write(result)





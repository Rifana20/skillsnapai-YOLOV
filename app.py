import streamlit as st
from llm_module import rewrite_text
from pdf_parser import extract_pdf_text, parse_profile
from image_analyzer import analyze_image
from networking_assistant import generate_message  # Optional fallback
import json

st.set_page_config(page_title="SkillSnap AI", layout="wide")
st.title("📊 SkillSnap AI - LinkedIn Optimizer")

# --- LinkedIn PDF Upload ---
st.header("📄 LinkedIn Profile Parser")
pdf_file = st.file_uploader("Upload your LinkedIn PDF Export", type=["pdf"], key="linkedin_pdf")

if pdf_file:
    text = extract_pdf_text(pdf_file)
    headline, about = parse_profile(text)

    st.subheader("Original Headline")
    st.write(headline)
    st.subheader("Optimized Headline")
    improved_headline = rewrite_text(headline, task="headline")
    st.write(improved_headline)

    st.subheader("Original About Section")
    st.write(about)
    st.subheader("Improved About Section")
    improved_about = rewrite_text(about, task="about")
    st.write(improved_about)

# --- Image Analysis ---
st.header("📸 Profile Picture Analyzer")
image_file = st.file_uploader("Upload your profile picture", type=["jpg", "png", "jpeg"], key="profile_image")

if image_file:
    st.write("✅ Image file uploaded successfully.")
    with st.spinner("Detecting faces..."):
        try:
            person_count, analysis = analyze_image(image_file)
            st.write(f"🧍 Detected people in image: {person_count}")
        except Exception as e:
            st.error(f"Image analysis failed: {e}")

# --- AI-based Networking Assistant ---
st.header("💬 Networking Assistant")
st.caption("🤖 Get a customized LinkedIn connection message generated using AI.")

role = st.text_input("Enter your target role (e.g., Web Developer, Data Scientist, Dancer)")

if st.button("Suggest Message"):
    if role.strip():
        with st.spinner("Generating message using AI..."):
            prompt = (
                f"Write a concise and professional LinkedIn connection message for someone aspiring to be a {role}. "
                f"Make it friendly and specific to the career field."
            )
            message = rewrite_text(prompt, task="networking")
            st.success("Suggested Message")
            st.code(message, language='markdown')
    else:
        st.warning("Please enter a valid role.")

import streamlit as st
from prompts import build_prompt
from content_generator import generate_content

# Page Configuration
st.set_page_config(
    page_title="Industry-Oriented Generative AI Content Creator",
    page_icon="✍️",
    layout="wide"
)

# Title
st.title("✍️ Industry-Oriented Generative AI Content Creation System")

st.markdown("""
Generate high-quality marketing and business content using
**Generative AI** and **Prompt Engineering**.
""")

# Sidebar
st.sidebar.header("Project Information")

st.sidebar.write("""
This application generates professional marketing and business content.

Supported Content Types:
- Blog Post
- Product Description
- Social Media Caption
- Advertisement Copy
- Email Campaign
- Business Proposal
""")

# Content Type
content_type = st.selectbox(
    "Select Content Type",
    [
        "Blog Post",
        "Product Description",
        "Social Media Caption",
        "Advertisement Copy",
        "Email Campaign",
        "Business Proposal"
    ]
)

# Audience
audience = st.text_input(
    "Target Audience",
    placeholder="Example: Small Business Owners"
)

# Tone
tone = st.selectbox(
    "Select Tone",
    [
        "Professional",
        "Friendly",
        "Persuasive",
        "Formal",
        "Casual",
        "Motivational"
    ]
)

# Product
product = st.text_area(
    "Product / Service",
    placeholder="Example: AI-Powered Accounting Software"
)

# Keywords
keywords = st.text_input(
    "SEO Keywords",
    placeholder="Example: AI accounting, automated bookkeeping"
)

# Generate Button
if st.button("Generate Content"):

    if not audience or not product or not keywords:

        st.warning("Please complete all fields.")

    else:

        prompt = build_prompt(
            content_type,
            audience,
            tone,
            product,
            keywords
        )

        with st.spinner("Generating content..."):

            content = generate_content(prompt)

        st.success("Content Generated Successfully!")

        st.subheader("Generated Content")

        st.markdown(content)

        # Save to file
        with open(
            "generated_content.txt",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(content)

        st.download_button(
            label="Download Content",
            data=content,
            file_name="generated_content.txt",
            mime="text/plain"
        )
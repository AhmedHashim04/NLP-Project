import streamlit as st
from summarization_core import summarize_text, analyze_sentiment
from fetch_text_from_url import fetch_text
from data_processing import clean_text
from collections import Counter
import matplotlib.pyplot as plt
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

st.set_page_config(page_title="Text Summarizer", layout="centered")
st.markdown(
    """
    <style>
        .main {background-color: #1e1e1e; padding: 20px; border-radius: 10px;}
        .stButton>button {background-color: #4CAF50; color: white; border-radius: 5px; border: none; padding: 10px;}
        .stTextInput>div>input, .stTextArea>div>textarea {
            border-radius: 5px; background-color: #2c2c2c; color: #ffffff; border: 1px solid #4CAF50;
        }
        h1 {color: #ffffff; text-align: center;}
        .stSlider>div {width: 50%; margin: auto;}
        body, .stMarkdown, .stRadio>label, .stSlider>label {color: #d3d3d3;}
        .stSpinner>div {color: #4CAF50;}
        .stRadio>div {background-color: #2c2c2c; border-radius: 5px; padding: 10px;}
        .stImage {background-color: #2c2c2c; border-radius: 5px;}
    </style>
""",
    unsafe_allow_html=True,
)

st.title("📝 Text Summarizer")
st.write("Paste text or enter a URL to summarize and analyze sentiment.")


def main():
    option = st.radio("Choose Input:", ("Paste Text", "Enter URL"), horizontal=True)
    num_sentences = st.slider(
        "Number of Summary Sentences:",
        1,
        5,
        3,
        help="Select how many sentences for the summary.",
    )

    text = ""
    if option == "Paste Text":
        text = st.text_area(
            "Enter Text:", height=150, placeholder="Paste your text here..."
        )
    else:
        url = st.text_input("Enter URL:", placeholder="https://example.com")
        if st.button("Fetch Text"):
            try:
                with st.spinner("Fetching text..."):
                    text = fetch_text(url)
                    st.text_area("Fetched Article:", text, height=150)
            except Exception as e:
                st.error(f"Error fetching text: {e}")
                logger.error(f"Fetch error: {e}")

    if text and st.button("Analyze Text"):
        try:
            with st.spinner("Analyzing..."):
                summary = summarize_text(text, num_sentences)
                sentiment, polarity = analyze_sentiment(summary)

                st.markdown(f"**Summary ({num_sentences} sentences):** {summary}")
                st.markdown(f"**Sentiment:** {sentiment} (Polarity: {polarity:.2f})")

                words = clean_text(text)
                freq = Counter(words).most_common(5)
                labels, values = zip(*freq)

                plt.figure(figsize=(8, 4))
                plt.bar(labels, values, color="#4CAF50")
                plt.xticks(rotation=30)
                plt.title("Top 5 Word Frequencies")
                plt.xlabel("Words")
                plt.ylabel("Frequency")
                plt.style.use("dark_background")
                plt.savefig("word_freq.png")
                st.image("word_freq.png")
                plt.close()
        except Exception as e:
            st.error(f"Analysis failed: {e}")
            logger.error(f"Analysis error: {e}")


if __name__ == "__main__":
    logger.info("App started.")
    main()

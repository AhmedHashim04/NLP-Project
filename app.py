import streamlit as st
from summarization_core import summarize_text, analyze_sentiment
from fetch_text_from_url import fetch_text
from data_processing import clean_text
from collections import Counter
import matplotlib.pyplot as plt
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

st.set_page_config(page_title="Text Summarizer", layout="wide")

st.markdown(
    """
    <style>
        body { background-color: #121212; color: #E0E0E0; }
        .block-container {
            padding: 2rem;
            background-color: #1e1e1e;
            border-radius: 10px;
        }
        h1, h2, h3, h4, h5 {
            color: #FFFFFF;
            text-align: center;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 10px;
            font-weight: bold;
            cursor: pointer;
        }
        .stTextInput>div>input, .stTextArea>div>textarea {
            background-color: #2c2c2c;
            color: #ffffff;
            border: 1px solid #4CAF50;
            border-radius: 5px;
        }
        .stSlider>div { width: 80%; margin: auto; }
        .stRadio>div { background-color: #2c2c2c; border-radius: 10px; padding: 10px; }
        .stImage { background-color: #2c2c2c; border-radius: 10px; padding: 10px; }
    </style>
""",
    unsafe_allow_html=True,)

st.title("📝 Text Summarizer")
st.write("Paste some text or enter a URL to summarize it and analyze its sentiment.")


def fetch_text_from_url(url: str) -> str:
    try:
        with st.spinner("Fetching content..."):
            text = fetch_text(url)
        st.success("Text fetched successfully!")
        return text
    except Exception as e:
        st.error(f"Error fetching content: {e}")
        logger.error(f"Fetch error: {e}")
        return ""


def plot_word_frequency(words):
    from collections import Counter
    freq = Counter(words).most_common(5)
    if not freq:
        st.info("No words to display frequency.")
        return

    labels, values = zip(*freq)
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(8, 5), dpi=150)

    bars = ax.bar(labels, values, color="#4CAF50", edgecolor="white", linewidth=1.5)
    ax.set_title("Top 5 Word Frequencies", fontsize=14, color="#ffffff", pad=15)
    ax.set_xlabel("Words", fontsize=12, color="white")
    ax.set_ylabel("Frequency", fontsize=12, color="white")
    ax.tick_params(axis="x", labelrotation=30, labelsize=10, colors="white")
    ax.tick_params(axis="y", labelsize=10, colors="white")

    for bar in bars:
        height = bar.get_height()
        ax.annotate(
            f"{height}",
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 5),textcoords="offset points",ha="center",va="bottom",fontsize=9,color="white",)

    fig.tight_layout()
    fig.patch.set_facecolor("#1e1e1e")
    st.pyplot(fig)
    plt.close()


def main():
    option = st.radio("Choose Input Method:", ("Paste Text", "Enter URL"), horizontal=True)
    num_sentences = st.slider(
        "Summary Length (Number of Sentences):",1,5,3,help="Choose how many sentences you want in the summary.",)

    text = ""

    if option == "Paste Text":
        text = st.text_area(
            "Enter Text Below:",
            height=200,
            placeholder="Paste or type your text here...",)
        if "fetched_text" in st.session_state:
            st.session_state.pop("fetched_text")
    else:
        url = st.text_input("Enter URL:", placeholder="https://example.com")

        if st.button("Fetch Text") and url:
            fetched = fetch_text_from_url(url)
            if fetched:
                st.session_state["fetched_text"] = fetched

        text = st.session_state.get("fetched_text", "")
        if text:
            st.text_area("Fetched Content:", text, height=200)

    analyze_clicked = st.button("Analyze")

    if text and analyze_clicked:
        try:
            with st.spinner("Generating summary and sentiment..."):
                summary = summarize_text(text, num_sentences)
                sentiment, polarity = analyze_sentiment(summary)

            st.subheader("📄 Summary")
            st.markdown(f"**{summary}**")

            st.subheader("💬 Sentiment Analysis")
            st.markdown(f"**Sentiment:** {sentiment}")
            st.markdown(f"**Polarity Score:** {polarity:.2f}")

            words = clean_text(text)
            plot_word_frequency(words)

            st.download_button("Download Summary", summary, file_name="summary.txt", mime="text/plain")

        except Exception as e:
            st.error(f"Analysis failed: {e}")
            logger.error(f"Analysis error: {e}")

    elif analyze_clicked:
        st.warning("Please enter or fetch some text to analyze.")

if __name__ == "__main__":
    logger.info("App started.")
    main()

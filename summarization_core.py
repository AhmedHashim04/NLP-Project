from .data_processing import clean_text, get_sentences
from collections import Counter
from textblob import TextBlob
import logging
from typing import List, Tuple

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def summarize_text(text: str, num_sentences: int = 3) -> str:
    if not text or not isinstance(text, str) or num_sentences < 1:
        logger.error("Invalid input.")
        raise ValueError("Text must be a non-empty string and sentences >= 1.")
    try:
        sentences = get_sentences(text)
        if not sentences:
            logger.warning("No sentences found.")
            raise ValueError("No sentences available.")
        if len(sentences) < num_sentences:
            num_sentences = len(sentences)
        words = clean_text(text)
        word_freq = Counter(words)
        scores = {
            i: sum(word_freq.get(w, 0) for w in clean_text(s))
            for i, s in enumerate(sentences)
        }
        top_indices = sorted(scores, key=scores.get, reverse=True)[:num_sentences]
        top_indices.sort()
        summary = " ".join(sentences[i] for i in top_indices)
        logger.info(f"Created summary with {len(top_indices)} sentences.")
        return summary
    except Exception as e:
        logger.error(f"Summarization failed: {e}")
        raise


def analyze_sentiment(text: str) -> Tuple[str, float]:
    if not text or not isinstance(text, str):
        logger.error("Invalid text.")
        raise ValueError("Text must be a non-empty string.")
    try:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        sentiment = (
            "Positive 😊"
            if polarity > 0
            else "Negative 😞" if polarity < 0 else "Neutral 😐"
        )
        logger.info(f"Sentiment: {sentiment}, Polarity: {polarity:.2f}")
        return sentiment, polarity
    except Exception as e:
        logger.error(f"Sentiment analysis failed: {e}")
        raise

from data_processing import clean_text, get_sentences
from collections import Counter
from textblob import TextBlob
from typing import List, Tuple
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def summarize_text(text: str, num_sentences: int = 3) -> str:
    if not text or not isinstance(text, str) or num_sentences < 1:
        logger.error("Invalid input for summarization.")
        raise ValueError("Text must be a non-empty string and num_sentences >= 1.")

    sentences: List[str] = get_sentences(text)
    if not sentences:
        logger.warning("No sentences found for summarization.")
        raise ValueError("No sentences available for summarization.")

    if len(sentences) < num_sentences:
        num_sentences = len(sentences)

    words: List[str] = clean_text(text)
    word_freq: Counter = Counter(words)

    sentence_scores = {}
    for i, sentence in enumerate(sentences):
        sentence_words = clean_text(sentence)
        score = sum(word_freq.get(word, 0) for word in sentence_words)
        sentence_scores[i] = score

    top_indices = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[
        :num_sentences
    ]
    top_indices.sort()

    summary = " ".join(sentences[i] for i in top_indices)
    logger.info(f"Summary generated with {num_sentences} sentences.")
    return summary


def analyze_sentiment(text: str) -> Tuple[str, float]:
    if not text or not isinstance(text, str):
        logger.error("Invalid text input for sentiment analysis.")
        raise ValueError("Text must be a non-empty string.")

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive 😊"
    elif polarity < 0:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"

    logger.info(f"Sentiment analysis: {sentiment} with polarity {polarity:.2f}")
    return sentiment, polarity

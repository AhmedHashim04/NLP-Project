import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from typing import List
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def setup_nltk():
    try:
        nltk.download("punkt", quiet=True)
        nltk.download("stopwords", quiet=True)
        logger.info("NLTK setup completed.")
    except Exception as e:
        logger.error(f"NLTK setup failed: {e}")
        raise


def clean_text(text: str) -> List[str]:
    if not text or not isinstance(text, str):
        raise ValueError("Text must be a non-empty string.")
    stop_words = set(stopwords.words("english") + list(string.punctuation))
    words = word_tokenize(text.lower())
    cleaned = [word for word in words if word not in stop_words]
    logger.info("Text cleaned.")
    return cleaned


def get_sentences(text: str) -> List[str]:
    if not text or not isinstance(text, str):
        raise ValueError("Text must be a non-empty string.")
    sentences = sent_tokenize(text)
    logger.info(f"Extracted {len(sentences)} sentences.")
    return sentences


setup_nltk()

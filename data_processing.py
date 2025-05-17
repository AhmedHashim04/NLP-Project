import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from typing import List
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def setup_nltk_resources():
    resources = ["punkt", "stopwords"]
    for resource in resources:
        try:
            nltk.data.find(f"tokenizers/{resource}")
        except LookupError:
            logger.info(f"Downloading NLTK resource: {resource}")
            nltk.download(resource, quiet=True)
    logger.info("NLTK resources are ready.")


setup_nltk_resources()

STOP_WORDS = set(stopwords.words("english")) | set(string.punctuation)


def clean_text(text: str) -> List[str]:
    if not text or not isinstance(text, str):
        raise ValueError("Text must be a non-empty string.")

    words = word_tokenize(text.lower())
    cleaned = [word for word in words if word not in STOP_WORDS]

    logger.info(f"Cleaned text with {len(cleaned)} words.")
    return cleaned


def get_sentences(text: str) -> List[str]:
    if not text or not isinstance(text, str):
        raise ValueError("Text must be a non-empty string.")

    sentences = sent_tokenize(text)
    logger.info(f"Extracted {len(sentences)} sentences.")
    return sentences

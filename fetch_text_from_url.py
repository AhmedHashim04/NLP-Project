import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def fetch_text(url: str) -> str:
    if not url or not isinstance(url, str):
        logger.error("Invalid URL.")
        raise ValueError("URL must be a non-empty string.")
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        text = " ".join(
            p.get_text().strip() for p in paragraphs if p.get_text().strip()
        )
        if not text:
            logger.warning(f"No text extracted from {url}.")
            raise ValueError("No text found in the webpage.")
        logger.info(f"Fetched text from {url}.")
        return text
    except Exception as e:
        logger.error(f"Fetch failed: {e}")
        raise

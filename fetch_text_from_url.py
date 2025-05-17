import requests
from bs4 import BeautifulSoup
import logging
from urllib.parse import urlparse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def is_valid_url(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme in ("http", "https"), result.netloc])
    except Exception:
        return False


def fetch_text(url: str, timeout: int = 10) -> str:
    if not url or not isinstance(url, str) or not is_valid_url(url):
        logger.error("Invalid URL provided.")
        raise ValueError("URL must be a valid non-empty string with http or https scheme.")

    try:
        headers = {"User-Agent": "Mozilla/5.0 (compatible; TextSummarizer/1.0)"}
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        texts = []
        for tag in ["p", "article", "div"]:
            elements = soup.find_all(tag)
            for elem in elements:
                txt = elem.get_text().strip()
                if txt and len(txt) > 30: 
                    texts.append(txt)

            if texts:
                break

        text = " ".join(texts).strip()

        if not text:
            logger.warning(f"No meaningful text found at {url}.")
            raise ValueError("No meaningful text found in the webpage.")

        logger.info(f"Fetched text from {url} ({len(text)} characters).")
        return text

    except requests.Timeout:
        logger.error("Request timed out.")
        raise
    except requests.HTTPError as e:
        logger.error(f"HTTP error: {e}")
        raise
    except Exception as e:
        logger.error(f"Failed to fetch text: {e}")
        raise

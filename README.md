# 📝 Text Summarizer with Sentiment Analysis

A sleek web application built with **Streamlit** that allows users to input text or provide a URL, then generates a concise summary of the text and performs sentiment analysis. The app also visualizes the top 5 most frequent words in the input text.

---

## Features

- Summarize any text or text fetched from a URL.
- Choose the number of sentences for the summary.
- Analyze sentiment (Positive, Negative, Neutral) with polarity score.
- Visualize the top 5 word frequencies in a clean, dark-themed interface.
- Responsive and user-friendly UI with custom styling.
- Robust error handling and informative logging.

---

## Project Structure

├── app.py # Main Streamlit app
├── summarization_core.py # Summarization and sentiment logic
├── data_processing.py # Text cleaning and sentence splitting
├── fetch_text_from_url.py# Web scraping utility to fetch text

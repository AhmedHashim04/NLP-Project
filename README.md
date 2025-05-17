# 📝 Text Summarizer with Sentiment Analysis

A powerful and intuitive web application built with **Flask** that enables users to input text or provide a URL, generating a concise summary and performing sentiment analysis. The app also provides insightful visualizations of the top 5 most frequent words in the input text, all within a modern, dark-themed interface.

---

## ✨ Features

- **Text Summarization**: Summarize any text or extract content from a URL with customizable summary length.
- **Sentiment Analysis**: Classify sentiment as Positive, Negative, or Neutral, along with a detailed polarity score.
- **Word Frequency Visualization**: Display the top 5 most frequent words in the input text using interactive bar charts.
- **Responsive UI**: Enjoy a sleek, user-friendly interface with custom styling and a dark theme.
- **Error Handling**: Robust error detection and informative logging for a seamless user experience.
- **Scalable Design**: Modular codebase for easy integration and future enhancements.

---

## 🛠️ Project Structure

```
├── app.py                  # Main Streamlit app
├── summarization_core.py   # Core logic for summarization and sentiment analysis
├── data_processing.py      # Utilities for text cleaning and sentence splitting
├── fetch_text_from_url.py  # Web scraping utility to fetch text from URLs
└── requirements.txt        # Python dependencies
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

0. Create and activate a virtual environment:

   - On Linux/MacOS:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - On Windows:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```


1. Clone the repository:
    ```bash
    cd venv
    git clone https://github.com/ALIADE1/NLP-Project.git
    mv NLP-Project src
    cd src
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    flask --app app.py run
    ```

---

## 📊 How It Works

1. **Input Options**: Enter text directly or provide a URL to fetch content.
2. **Summarization**: Choose the number of sentences for the summary.
3. **Sentiment Analysis**: Get sentiment classification and polarity score.
4. **Visualization**: View the top 5 most frequent words in an interactive chart.

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request. For major changes, please open an issue first to discuss your ideas.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🌟 Acknowledgments

- **NLTK** and **TextBlob** for natural language processing capabilities.
- Open-source libraries and the developer community for their invaluable contributions.

---

## 📬 Contact

For questions or feedback, reach out to [ahmedha4im7@gmail.com](mailto:ahmedha4im7@gmail.com).


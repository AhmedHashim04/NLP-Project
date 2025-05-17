from flask import Flask, request, render_template, jsonify
from summarization_core import summarize_text, analyze_sentiment
from fetch_text_from_url import fetch_text
from data_processing import clean_text
from collections import Counter
import matplotlib.pyplot as plt
import logging
import os

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        option = request.form['option']
        num_sentences = int(request.form['num_sentences'])
        if option == 'paste_text':
            text = request.form['text']
        else:
            url = request.form['url']
            try:
                text = fetch_text(url)
            except Exception as e:
                logger.error(f"Fetch error: {e}")
                return jsonify({'error': 'Error fetching text'}), 400

        try:
            summary = summarize_text(text, num_sentences)
            sentiment, polarity = analyze_sentiment(summary)

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
            plt.close()

            return jsonify({
                'summary': summary,
                'sentiment': sentiment,
                'polarity': polarity,
                'word_freq': os.path.join(os.getcwd(), 'word_freq.png')
            })
        except Exception as e:
            logger.error(f"Analysis error: {e}")
            return jsonify({'error': 'Analysis failed'}), 400

    return render_template('index.html')

if __name__ == '__main__':
    logger.info("App started.")
    app.run(debug=True)
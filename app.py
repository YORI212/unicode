from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # 👈 Allow all origins by default

responses = {
    "hello": ["Hi", "Hey", "Go away", "Yo"],
    "bye": ["Goodbye", "See ya", "Later"],
    "thanks": ["You're welcome", "No problem", "Anytime"],
    "default": ["Hmm", "Interesting...", "No idea", "Okay"]
}

@app.route('/')
def home():
    return "Random Word Response API is live!"

@app.route('/api/random-response', methods=['POST'])
def random_response():
    data = request.json
    user_word = data.get("word", "").lower()

    word_responses = responses.get(user_word, responses["default"])
    response = random.choice(word_responses)

    return jsonify({
        "input": user_word,
        "response": response
    })

if __name__ == '__main__':
    app.run(debug=True)

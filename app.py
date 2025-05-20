from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Dictionary mapping input words to possible responses
responses = {
    "hello": ["Hi", "Hey", "Go away", "Yo"],
    "bye": ["Goodbye", "See ya", "Later"],
    "thanks": ["You're welcome", "No problem", "Anytime"],
    "default": ["Hmm", "Interesting...", "No idea", "Okay"]
}

@app.route('/')
def home():
    return "Keyword-based random response API is running!"

@app.route('/api/random-response', methods=['POST'])
def random_response():
    data = request.json
    user_word = data.get("word", "").lower()

    # Choose response list based on input; fall back to 'default'
    word_responses = responses.get(user_word, responses["default"])
    response = random.choice(word_responses)

    return jsonify({
        "input": user_word,
        "response": response
    })

if __name__ == '__main__':
    app.run(debug=True)

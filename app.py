from flask import Flask, request, jsonify
from flask_cors import CORS
import npttf2utf
import os

app = Flask(__name__)
CORS(app)  # 👈 Allow all origins by default

RULES_JSON = os.environ.get('RULES_JSON', os.path.join(os.path.dirname(npttf2utf.__file__), 'map.json'))
font_mapper = npttf2utf.FontMapper(RULES_JSON)

# Try converting from Preeti to Unicode (this is the more common supported direction)






@app.route('/')
def home():
    return "Random Word Response API is live!"

@app.route('/api/random-response', methods=['POST'])
def random_response():
    data = request.json
    user_word = data.get("word", "")

    word_responses = font_mapper.map_to_unicode(user_word)


    return jsonify({
        "input": user_word,
        "response": word_responses
    })

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
import npttf2utf
import os

app = Flask(__name__)
CORS(app)

# Load rules
RULES_JSON = os.environ.get('RULES_JSON', os.path.join(os.path.dirname(npttf2utf.__file__), 'map.json'))
font_mapper = npttf2utf.FontMapper(RULES_JSON)

@app.route('/')
def home():
    return "Unicode Converter API is live!"

@app.route('/api/unicode', methods=['POST'])
def convert_to_unicode():
    data = request.json
    user_word = data.get("word", "")

    unicode_result = font_mapper.map_to_unicode(user_word)

    return jsonify({"converted": unicode_result})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, send_file
from rembg import remove
from PIL import Image
import io
import os

app = Flask(__name__)

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return {'error': 'No image uploaded'}, 400

    image = request.files['image']
    input_bytes = image.read()
    output_bytes = remove(input_bytes)

    return send_file(
        io.BytesIO(output_bytes),
        mimetype='image/png',
        as_attachment=True,
        download_name='no-bg.png'
    )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use the PORT environment variable
    app.run(host='0.0.0.0', port=port)        # Bind to 0.0.0.0 for external access

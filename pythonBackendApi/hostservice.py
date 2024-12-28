from flask import Flask, request, send_file
from flask_cors import CORS
from PIL import Image
import os
app = Flask(__name__)
CORS(app)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit
@app.route('/process_image', methods=['POST'])
def process_image():
    try:
        # Get the uploaded file
        file = request.files.get('file')

        if not file:
            return {"error": "No file provided"}, 400

        # Open the image file
        img = Image.open(file)

        # Process the image (grayscale)
        grayscale_img = img.convert("L")

        # Save the processed image to a temporary file
        temp_path = "processed_image.jpg"
        grayscale_img.save(temp_path)

        # Return the image file
        return send_file(temp_path, mimetype='image/jpeg')
    except Exception as e:
        return {"error": str(e)}, 500
    # finally:
    #     # Cleanup temporary file if exists
    #     if os.path.exists("processed_image.jpg"):
    #         os.remove("processed_image.jpg")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

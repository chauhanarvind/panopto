from flask import Flask, request, jsonify
from flask_cors import CORS
import lib

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

@app.route('/', methods=['POST'])
def download_video_mp4():
    data = request.json  
    url = data.get('url')

    if not url:
        return jsonify({'error': 'No URL provided'}), 400
    
    print("inside index.py")
    
    try:
        # Call getVideoType in lib.py, which will handle the video download
        lib.getVideoType(url)
        return jsonify({'message': 'Video downloaded successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)

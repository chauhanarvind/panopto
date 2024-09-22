"""main file for flask app"""
import os
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import lib


app = Flask(__name__)

# Allow requests from all origins
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['POST'])
def download_video_mp4():
    """route for home page"""
    data = request.json  
    url = data.get('url')

    if not url:
        return jsonify({'error': 'No URL provided'}), 400
    
    print("inside index.py")
    
    try:
        # Call getVideoType in lib.py, which will handle the video download
        file_path = lib.getVideoType(url)

        if file_path and os.path.exists(file_path):
            # Serve the file to the client
            response = send_file(file_path, as_attachment=True)

            # After serving the file, delete it from the server
            try:
                os.remove(file_path)  # File deletion after serving
                print(f"File {file_path} deleted from server")
            except Exception as e:
                print(f"Error deleting file: {e}")
            
            return response
        else:
            return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)

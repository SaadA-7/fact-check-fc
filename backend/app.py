from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys
from model_trainer import FakeNewsDetector

app = Flask(__name__)
CORS(app)

# Initialize the detector
detector = FakeNewsDetector()

# Load the model at startup
if not detector.load_model():
    print("No saved model found. Please train the model first.")
    sys.exit(1)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Soccer Fake News Detector API",
        "status": "running",
        "endpoints": {
            "/predict": "POST - Predict if news is fake or real"
        }
    })

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({
                "error": "Missing 'text' field in request body"
            }), 400
        
        text = data['text'].strip()
        
        if not text:
            return jsonify({
                "error": "Text cannot be empty"
            }), 400
        
        # Make prediction
        result = detector.predict(text)
        
        return jsonify({
            "success": True,
            "prediction": result['prediction'],
            "confidence": round(result['confidence'], 4),
            "probabilities": {
                "real": round(result['probabilities']['real'], 4),
                "fake": round(result['probabilities']['fake'], 4)
            }
        })
    
    except Exception as e:
        return jsonify({
            "error": f"Prediction failed: {str(e)}"
        }), 500

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "model_loaded": True
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
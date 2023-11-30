import sys
from flask import Flask, jsonify, request
sys.path.append('./Brain_Tumor_Classification')
from classifier import classify_image  # Import your machine learning module

app = Flask(__name__)

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        if request.method == 'POST':
            # Assuming you receive JSON data for prediction
            data = request.files
            
            # Perform image classification using your machine learning model
            pred = classify_image(data['file'])  # Adjust as needed
            
            # Return the prediction as a JSON response
            return jsonify({'prediction': str(pred)})

    except Exception as e:
        error = "Error: File can't be processed"
        return jsonify({'error': error})

if __name__ == "__main__":
    app.run(port=6000, debug=True)

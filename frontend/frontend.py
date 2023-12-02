from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Home route
@app.route("/")
def main():
    return render_template("index.html")

# Prediction route
@app.route('/prediction', methods=['POST'])
def predict_image_file():
    try:
        if request.method == 'POST':
            # Get the image file from the request
            image_file = request.files['file'].stream

            # Send a request to the Flask backend on port 6000 for prediction
            response = requests.post("http://127.0.0.1:6000/predict", files={'file': image_file})

            if response.status_code == 200:
                # Get the prediction from the response
                prediction = response.json()['prediction']
                return render_template("result.html", predictions=str(prediction))
            else:
                error = "Error in prediction request."
                return render_template("result.html", err=error)

    except Exception as e:
        error = "Error: File can't be processed"
        
        return render_template("result.html", err=error)

if __name__ == "__main__":
    app.run(port=5000, debug=True)

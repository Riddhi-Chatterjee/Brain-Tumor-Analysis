from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route('/prediction', methods=['POST'])
def predict_image_file():
    try:
        if request.method == 'POST':
            # Assuming you have a form with a file input named 'file'
            image_file = request.files['file']

            # Sending a request to your backend for prediction
            response = requests.post("http://127.0.0.1:6000/predict", files={'file': image_file})

            if response.status_code == 200:
                # Getting the prediction from the response
                prediction = response.json().get('prediction', 'Error: No prediction received')
                return render_template("result.html", predictions=str(prediction))
            else:
                error = "Error in prediction request. Status code: {}".format(response.status_code)
                return render_template("result.html", err=error)

    except Exception as e:
        error = "Error: File can't be processed"
        return render_template("result.html", err=error)

if __name__ == "__main__":
    app.run(port=5000, debug=True)

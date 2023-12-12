from flask import Flask, render_template, request, send_file
import requests
import logging
import sys

app = Flask(__name__)

log_file_path = './logs/log_output.log'

formatter = logging.Formatter('%(asctime)s %(message)s')  # Setting the desired log format

app.logger.setLevel(logging.INFO)  # Set log level to INFO
handler = logging.FileHandler(log_file_path)  # Log to the file
handler.setFormatter(formatter)
app.logger.addHandler(handler)

log_dict = {
    'Predicted tumor type: glioma': 'Glioma',
    'Predicted tumor type: meningioma': 'Meningioma',
    'No tumor was detected': 'No tumor',
    'Predicted tumor type: pituitary': 'Pituitary'
}

@app.route("/")
def main():
    return render_template("index.html")

@app.route('/prediction', methods=['POST'])
def predict_image_file():
    image_file = "NULL"
    try:
        if request.method == 'POST':
            image_file = request.files['file']

            # Sending a request to our backend for prediction
            response = ""
            if len(sys.argv) == 2 and sys.argv[1] == 'no_cont':
                response = requests.post("http://127.0.0.1:3500/predict", files={'file': image_file})
            else:
                response = requests.post("http://bta-backend:3500/predict", files={'file': image_file})

            if response.status_code == 200:
                # Getting the prediction from the response
                prediction = response.json().get('prediction', 'Error: No prediction received')
                if str(prediction) in log_dict.keys():
                    app.logger.info("Prediction for MRI image %s:  %s",str(image_file), log_dict[str(prediction)].replace(" ", "_"))
                else:
                    app.logger.info("Prediction for MRI image %s:  %s",str(image_file), str(prediction).replace(" ", "_"))
                return render_template("result.html", predictions=str(prediction))
            else:
                error = "Error in prediction request. Status code: {}".format(response.status_code)
                app.logger.info("Prediction for MRI image %s:  %s",str(image_file), error.replace(" ", "_"))
                return render_template("result.html", err=error)

    except Exception as e:
        error = "Error: File can't be processed."
        app.logger.info("Prediction for MRI image %s:  %s",str(image_file), error.replace(" ", "_"))
        return render_template("result.html", err=error)
    
@app.route('/download_file')
def download_file():
    # Specifying the path to the log file
    file_path = './logs/log_output.log'

    # Setting the filename as it will appear on the user's machine
    filename = 'log_output.log'

    return send_file(file_path, as_attachment=True, download_name=filename)

if __name__ == "__main__":
    app.run(port=3000, debug=True, host='0.0.0.0')

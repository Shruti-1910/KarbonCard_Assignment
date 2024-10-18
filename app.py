from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
from model import probe_model_5l_profit

app = Flask(__name__)

# Global variable to store the result from model.py
model_result = None

# Route for Page 1: Upload and Submit
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    global model_result
    if request.method == 'POST':
        file = request.files['datafile']
        if file:
            # Read the file and process the data
            data = json.load(file)
            # Call the financial model from model.py
            model_result = probe_model_5l_profit(data["data"])
            # Redirect to the results page
            return redirect(url_for('display_results'))
    return render_template('upload.html')

# Route for Page 2: Display Results
@app.route('/results', methods=['GET'])
def display_results():
    global model_result
    if model_result:
        return render_template('results.html', result=model_result)
    else:
        return redirect(url_for('upload_file'))

if __name__ == '__main__':
    app.run(debug=True)

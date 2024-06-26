from flask import Flask, jsonify, render_template
import os
import pandas as pd

app = Flask(__name__)

# Get the directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the relative path to the dataset
file_path = os.path.join(current_dir, '..', 'tv_cleaned_data.csv')

# Load dataset
data = pd.read_csv(file_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    # Add your data processing code here
    return jsonify({"message": "Data route"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

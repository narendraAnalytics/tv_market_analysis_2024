from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    # Add your data processing code here
    return jsonify({"message": "Data route"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

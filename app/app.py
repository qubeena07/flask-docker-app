import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello, Dockerized Flask API!"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}),200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
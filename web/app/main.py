from flask import Flask, url_for, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(status='ok',message='Hi there')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

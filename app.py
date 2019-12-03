import os
import models
from flask import Flask, request, jsonify, g
from flask_cors import CORS

DEBUG = True
PORT = 8000

app = Flask(__name__)

@app.route('/')
def index():
    return 'hi'

if __name__ == '__main__':
    # models.initialize()
    app.run(debug=DEBUG, port=PORT)
import os
import models
from flask import Flask, request, jsonify, g
from flask_cors import CORS

DEBUG = True
PORT = 8000

app = Flask(__name__)

@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response

@app.route('/')
def index():
    return 'hi'

app.register_blueprint(user, url_prefix='/api/v1/user')

if __name__ == '__main__':
    # models.initialize()
    app.run(debug=DEBUG, port=PORT)
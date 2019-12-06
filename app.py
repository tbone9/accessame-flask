import os
import models
from flask import Flask, request, jsonify, g
from flask_cors import CORS
from flask_login import LoginManager
from resources.users import user
from resources.places import place

DEBUG = True
PORT = 8000

app = Flask(__name__)

app.secret_key = ';laskjfla;skfjower;lksf'
app.cors_headers = 'Content-Type'
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    try:
        return models.User.get(models.User.id == user_id)
    except models.DoesNotExist:
        return None

@login_manager.unauthorized_handler
def unauthorized():
  return jsonify(data={
      'error': 'User not logged in.'
    }, status={
      'code': 401,
      'message': "You must be logged in to access that resource."
    }), 401

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

CORS(user, origins=['http://localhost:3000', 'https://accessame-react.herokuapp.com'], supports_credentials=True)
app.register_blueprint(user, url_prefix='/api/v1/user')

CORS(place, origins=['http://localhost:3000', 'https://accessame-react.herokuapp.com'], supports_credentials=True)
app.register_blueprint(place, url_prefix='/api/v1/place')

if 'ON_HEROKU' in os.environ:
    print('hitting ')
    models.initialize()

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
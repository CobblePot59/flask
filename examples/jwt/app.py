from flask import Flask
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_pyfile('config.py')

jwt = JWTManager(app)

from views import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config.from_pyfile('config.py')

socketio = SocketIO(app)

from views import *

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=80)

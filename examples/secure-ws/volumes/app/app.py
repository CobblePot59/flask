from flask import Flask
from flask_socketio import SocketIO


app = Flask(__name__)

socketio = SocketIO(app)

from views import *

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, ssl_context=('/etc/ssl/certs/secure-ws.cobblepot59.int.crt', '/etc/ssl/certs/secure-ws.cobblepot59.int.key'))

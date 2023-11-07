from flask import render_template
from app import app, socketio

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('server_event')
def event(message):
    # Reveive an event from the client
    print(message)

    # Send an event to the client
    socketio.emit('client_event', 'Hello, client');


from flask import render_template
from app import app, socketio

def notify(message, toast_type):
    socketio.emit('toast', {'message': message, 'type': toast_type})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info', methods=['POST'])
def info():
    notify('This is an example of info toast', 'info')
    return '', 204

@app.route('/success', methods=['POST'])
def success():
    notify('This is an example of success toast', 'success')
    return '', 204

@app.route('/warning', methods=['POST'])
def warning():
    notify('This is an example of warning toast', 'warning')
    return '', 204

@app.route('/error', methods=['POST'])
def error():
    notify('This is an example of error toast', 'error')
    return '', 204

from flask import render_template, request, redirect, url_for, session, flash
from app import app, ldap
from decor import login_required

def notify(message, toast_type):
    socketio.emit('toast', {'message': message, 'type': toast_type})

@app.route('/', methods=['GET'])
@login_required
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('status'):
        return redirect(url_for('index'))

    if request.method == 'GET':
       return render_template('login.html')

    login = request.form['login']
    password = request.form['password']
    if ldap.authenticate(login, password):
        session.update({'status':True, 'login':login})
        return redirect(url_for('index'))
    else:
        flash('Bad Login', 'error')
        return redirect(url_for('login'))

@app.route("/logout", methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('login'))


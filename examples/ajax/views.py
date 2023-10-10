from flask import render_template, request, jsonify
from app import app

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        pbutton_value = request.form['pbutton_key']
        return jsonify(f'I received {pbutton_value}')

    gbutton_value = request.args.get('gbutton_key')
    return jsonify(f'I received {gbutton_value}')

from flask import Flask, render_template, jsonify,redirect, url_for
import random
import json

app = Flask(__name__)

@app.route('/')
def home():
    # redirect to register page
    return redirect(url_for('register'))


@app.route('/register')
def register():
    return render_template('register.html')




@app.route('/regions')
def regions():
    import os
    # get current working directory
    cwd = os.getcwd()
    path = os.path.join(cwd, '27_flask_fetch_address', 'table_region.json')
    with open(path, 'r') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/provinces')
def provinces():
    import os
    cwd = os.getcwd()
    path = os.path.join(cwd, '27_flask_fetch_address', 'table_province.json')
    
    with open(path) as f:
        data = json.load(f)

    return jsonify(data)


@app.route('/municipalities')
def municipalities():
    import os
    cwd = os.getcwd()
    path = os.path.join(cwd, '27_flask_fetch_address', 'table_municipality.json')
    
    with open(path) as f:
        data = json.load(f)

    return jsonify(data)

@app.route('/barangays')
def barangays():
    import os
    cwd = os.getcwd()
    path = os.path.join(cwd, '27_flask_fetch_address', 'table_barangay.json')
    
    with open(path) as f:
        data = json.load(f)

    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True)
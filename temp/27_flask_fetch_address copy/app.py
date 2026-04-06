from flask import Flask, render_template, jsonify
import random
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', message="hello user")

@app.route('/help')
def help():
    # generate random int on page load
    random_number = random.randint(1, 100)
    return render_template('help.html', random_number=random_number)

@app.route('/about')
def about():
    data = {'name': 'John Doe', 'age': 30, 'city': 'New York'}
    return render_template('about.html', data=data)

@app.route('/random')
def random_page():
    return render_template('random.html')

@app.route('/generate_random', methods=['POST'])
def generate_random():
    random_number = random.randint(1, 100)
    return jsonify(number=random_number)



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
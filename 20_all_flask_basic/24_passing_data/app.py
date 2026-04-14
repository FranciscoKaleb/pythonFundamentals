from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', message="hello user")

@app.route('/help')
def help():
    # generate random int
    from random import randint
    random_number = randint(1, 100)
    return render_template('help.html', random_number=random_number)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
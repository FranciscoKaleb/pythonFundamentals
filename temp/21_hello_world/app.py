from flask import Flask, render_template

# this code creates a Flask application instance and defines a route for the home page. 
# When the user visits the root URL ('/'), the 'home' function is called, 
# which renders the 'index.html' template. Finally, the application is run in debug mode, 
# allowing for easier development and debugging.
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# you can keep adding more routes and functions here to handle different URLs and logic for your application.


# this block checks if the script is being run directly (as the main program) and, 
# if so, it starts the Flask development server with debugging enabled.
# dont delete this block, it is necessary to run the application
if __name__ == '__main__':
    app.run(debug=True)


# pip install flask
# py -m pip install flask
# python -m pip install flask


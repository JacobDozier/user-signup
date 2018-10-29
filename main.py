from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # Displays runtime errors in the browser, too



@app.route("/signup", methods=['POST'])
def user_signup():
    username_input = request.form['username']
    email_input = request.form['email']

    # Return user input in username and email fields
    return render_template('index.html', username=username_input, email=email_input)

@app.route("/")
def index():
    return render_template('index.html', )

app.run()
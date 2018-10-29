from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # Displays runtime errors in the browser, too

@app.route("/signup", methods=['POST'])
def user_signup():
    return render_template('index.html')

@app.route("/")
def index():
    return render_template('index.html', )

app.run()
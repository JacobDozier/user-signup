from flask import Flask, request, redirect, render_template
import cgi, helpers

app = Flask(__name__)

app.config['DEBUG'] = True      # Displays runtime errors in the browser, too

@app.route("/", methods=['POST'])
def user_signup():
    username_input = cgi.escape(request.form['username'])
    pass_input = cgi.escape(request.form['password'])
    verify_pass_input = cgi.escape(request.form['verify'])
    email_input = cgi.escape(request.form['email'])
    is_user_blank = False
    is_user_invalid = False
    is_pass_blank = False
    pass_mismatch = False
    is_email_invalid = False

    is_user_blank = helpers.is_user_blank(username_input)
    is_user_invalid = helpers.is_user_invalid(username_input)
    is_pass_blank = helpers.is_pass_blank(pass_input)
    pass_mismatch = helpers.pass_mismatch(pass_input, verify_pass_input)
    is_email_invalid = helpers.is_email_valid(email_input)

   # Check to see if user input is valid, then mark global variable to trigger new form.
    if not is_user_blank and not is_user_invalid and not is_pass_blank and not pass_mismatch and not is_email_invalid:
       return redirect("/welcome?username={}".format(username_input))

    if is_user_blank:
        blank_user_error = "Username is required."
        if is_pass_blank:
            blank_pass_error = "That's an invalid password."
            if is_email_invalid:
                email_error = "That's an invalid email."
                return render_template('index.html', username=username_input, email=email_input, email_error=email_error, pass_error=blank_pass_error, user_error=blank_user_error)
            return render_template('index.html', username=username_input, email=email_input, user_error=blank_user_error, pass_error=blank_pass_error)
        elif pass_mismatch:
            verify_pass_error = "Password does not match. Please retype password exactly."
            if is_email_invalid:
                email_error = "That's an invalid email."
                return render_template('index.html', username=username_input, email=email_input, email_error=email_error, pass_error=verify_pass_error, user_error=blank_user_error)
            return render_template('index.html', username=username_input, email=email_input, user_error=blank_user_error, verify_pass_error=verify_pass_error)

        return render_template('index.html', username=username_input, email=email_input, user_error=blank_user_error)
    elif is_user_invalid:
        invalid_user_error = "That's not a valid username."
        if is_pass_blank:
            blank_pass_error = "That's an invalid password."
            if is_email_invalid:
                email_error = "That's an invalid email."
                return render_template('index.html', username=username_input, email=email_input, email_error=email_error, user_error=invalid_user_error, pass_error=blank_pass_error)
            return render_template('index.html', username=username_input, email=email_input, user_error=invalid_user_error, pass_error=blank_pass_error)
        elif pass_mismatch:
            verify_pass_error = "Password does not match. Please retype password exactly."
            if is_email_invalid:
                email_error = "That's an invalid email."
                return render_template('index.html', username=username_input, email=email_input, email_error=email_error, pass_error=verify_pass_error, user_error=invalid_user_error)
            return render_template('index.html', username=username_input, email=email_input, user_error=blank_user_error, verify_pass_error=verify_pass_error)

        return render_template('index.html', username=username_input, email=email_input, user_error=invalid_user_error)

    if is_pass_blank:
        blank_pass_error = "That's an invalid password."
        if is_email_invalid:
            email_error = "That's an invalid email."
            return render_template('index.html', username=username_input, email=email_input, email_error=email_error, pass_error=blank_pass_error)
        return render_template('index.html', username=username_input, email=email_input, pass_error=blank_pass_error)
    elif pass_mismatch:
        verify_pass_error = "Password does not match. Please retype password exactly."
        if is_email_invalid:
            email_error = "That's an invalid email."
            return render_template('index.html', username=username_input, email=email_input, email_error=email_error, pass_error=verify_pass_error)
        return render_template('index.html', username=username_input, email=email_input, verify_pass_error=verify_pass_error)
    
    if is_email_invalid:
        email_error = "That's an invalid email."
        return render_template('index.html', username=username_input, email=email_input, email_error=email_error)

    return render_template('index.html', username=username_input, email=email_input)

@app.route("/welcome", methods=['GET'])
def welcome_message():
    username_input = cgi.escape(request.args['username'])
    return render_template('welcome.html', username=username_input)

@app.route("/")
def index():
    return render_template('index.html')

app.run()
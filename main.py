from flask import Flask, request, redirect, render_template
import cgi, helpers

app = Flask(__name__)

app.config['DEBUG'] = True      # Displays runtime errors in the browser, too


# Need to create helpers.py and create logic to test bools assigned based on function call.
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

    #HERE
    if is_user_blank:
        blank_user_error = "Username is required."
        if is_pass_blank:
            blank_pass_error = "Password is required."
            return render_template('index.html', email=email_input, user_error=blank_user_error,pass_error=blank_pass_error)
        elif pass_mismatch:
            verify_pass_error = "Password does not match. Please retype password exactly."
            return render_template('index.html', email=email_input, user_error=blank_user_error, verify_pass_error=verify_pass_error)

        return render_template('index.html', email=email_input, user_error=blank_user_error)
    elif is_user_invalid:
        invalid_user_error = "That's not a valid username."
        return render_template('index.html', email=email_input, user_error=invalid_user_error)

    #HERE
    if is_pass_blank:
        blank_pass_error = "Password is required."
        return render_template('index.html', username=username_input, email=email_input, pass_error=blank_pass_error)
    elif pass_mismatch:
        verify_pass_error = "Password does not match. Please retype password exactly."
        return render_template('index.html', username=username_input, email=email_input, verify_pass_error=verify_pass_error)
    
    # Still need to add email validation to other logic trees. #HERE
    if is_email_invalid:
        email_error = "That's an invalid email."
        return render_template('index.html', username=username_input, email=email_input, email_error=email_error)

    # Return user input in username and email fields
    return render_template('index.html', username=username_input, email=email_input)

@app.route("/")
def index():
    return render_template('index.html', )

app.run()
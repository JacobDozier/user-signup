def is_user_blank(username_input):
    if username_input == "":
        return True

def is_user_invalid(username_input):
    if len(str(username_input)) < 3 or len(str(username_input)) > 20:
        return True

def is_pass_blank(pass_input):
    if pass_input == "":
        return True
    if len(pass_input) < 3 or len(pass_input) > 20:
        return True

def pass_mismatch(pass_input, verify_pass_input):
    if pass_input != verify_pass_input:
        return True

def is_email_valid(email_input):
    if email_input != "":
        if email_input.count('@') > 1 or email_input.count('@') == 0 or email_input.count('.') > 1 or email_input.count('.') == 0:
                return True
        if len(str(email_input)) < 3 or len(str(email_input)) > 20:
                return True
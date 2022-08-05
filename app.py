from flask import Flask, request, flash, make_response, render_template, redirect, url_for

from user_management import add_user, get_user_details, get_user_with_credentials

from utils import should_be_signed_in,  should_be_signed_out, get_query_values, get_form_values, get_account_creation_error

from config import FLASK_SECRET, FLASK_DEBUG

app = Flask(__name__)
app.secret_key = FLASK_SECRET


@app.get('/')
@should_be_signed_in
def view_feed():
    current_user_id = int(request.cookies.get('user_id'))
    return render_template('feed.html')


@app.get('/signup')
@should_be_signed_out
def view_signup():
    return render_template('signup.html')


@app.post('/signup')
@should_be_signed_out
def submit_signup():
    firstname, lastname, username, email, dob, password, gender, profile = get_form_values('firstname', 'lastname', 'username', 'email', 'dob', 'password', 'gender', 'profile')
    if error := get_account_creation_error(firstname, lastname, username, email, dob, password, gender, profile):
        flash(error)
        return redirect(url_for(view_signup.__name__))
    add_user(firstname, lastname, username, email, dob, password, gender, profile)
    return redirect(url_for(view_signin.__name__))


@app.get('/signin')
@should_be_signed_out
def view_signin():
    return render_template('signin.html')


@app.post('/signin')
@should_be_signed_out
def submit_signin():
    username, password = get_form_values('username', 'password')
    response = make_response(redirect(url_for(view_signin.__name__)))
    if (user_id := get_user_with_credentials(username, password)) is None:
        flash('Invalid details, please try again')
    else:
        response.set_cookie('user_id', str(user_id), max_age=3600)
    return response


@app.post('/signout')
@should_be_signed_in
def submit_signout():
    response = make_response(redirect(url_for(view_signin.__name__)))
    response.delete_cookie('user_id')
    return response


app.run(debug=FLASK_DEBUG)
from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]*$')
PASSWORD_REGEX = re.compile(r'^[a-zA-Z0-9]{8,}$')
app = Flask(__name__)
app.secret_key = "mySecret!"

@app.route('/', methods=['GET'])
def quotes():
  return render_template("quotes.html")


@app.route('/process', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")

    if len(request.form['name'])<1:
        flash("name cannot be blank!")
    elif not NAME_REGEX.match(request.form['name']) and len(request.form['name']) < 2:
        flash("Name should be letters, provide atleast 2!")

    if len(request.form['alias'])<1:
        flash("alias cannot be blank!")

    if len(request.form['password'])<8:
        flash("password should be more than 8 characters")
    elif not PASSWORD_REGEX.match(request.form['password']):
        flash("Please provide a strong password, atleast 8!")

    if len(request.form['confirm_password'])<1:
        flash('confirm_password should mach password' )
    elif not PASSWORD_REGEX.match(request.form['confirm_password']) and (password != confirm_password):
        flash("Confirm password should match original password")

    if len(request.form['login']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['login']):
        flash("Invalid Email Address!")

    if len(request.form['password_login'])<8:
        flash("password should be more than 8 characters")
    elif not PASSWORD_REGEX.match(request.form['password_login']):
        flash("Please provide a strong password, atleast 8!")

    else:
        flash("Thanks for your registration/login.")
    return redirect('/')







app.run(debug=True)

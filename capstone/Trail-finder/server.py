from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
# import curd

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "mycapstoneproject"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """View homepage."""

    return render_template("home.html")

@app.route("/sign_up")
def sign_up():
    """View sign_up page."""

    return render_template("sign_up.html")

@app.route("/login")
def login():
    """View login page."""

    return render_template("login.html")


@app.route("/submit", methods=['POST'])
def submit():
    if request.method == 'POST':
        # email = request.form['email']
        # password = request.form['password']
        email = request.form.get('email')
        password = request.form.get('password')

    if email == '' or password == '':
       return render_template('login.html', message = "Please enter required fields")

    return render_template('success.html')

@app.route("/register", methods=['POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('fname')
        last_name = request.form.get('lname')
        email_add = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')

    if first_name == '' or last_name == '' or email_add == '' or password == '' or confirm_password == '':
        return render_template('sign_up.html', message = "Please enter all required fields")

    user = curd.get_user_by_email(email_add)
    if user:
        flash("Cannot create an account with that email. User already exists. Try again.")
    else:
        user = crud.create_user(first_name, last_name, email_add, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")
    # return render_template('success.html')
    return redirect("/")



# Check this function
@app.route("/logout", methods=['POST'])
def logout():
    """User logout"""

    return render_template(url_for(homepage)) 
    
# Create comment

# Updat comment
# Delete comment
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
from flask import Flask, render_template, request, flash
import sqlite3

#flask
app = Flask(__name__)
app.secret_key = "123233232t4443435345"

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/create-account")
def createAccount():
    return render_template("create-account.html", title="Create Account")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    db = sqlite3.connect("logins.db")
    c = db.cursor()

    #check if username and pass are in sql database
    accounts = c.execute("SELECT * FROM logins WHERE username = :username AND password = :password", {"username" : username, "password" : password})

    num_of_accounts = 0
    for account in accounts:
        num_of_accounts += 1
    if(num_of_accounts == 1):
        db.close()
        return "<h1 style='color:green'>Successfully Logged In</h1>"
    db.close()
    return "<h1 style='color:red'>Log In Failed</h1>"



@app.route("/register", methods=["POST"])
def register():

    db = sqlite3.connect("logins.db")
    c = db.cursor()

    username = request.form.get("username")
    password = request.form.get("password")

    c.execute("INSERT INTO logins (username, password) VALUES (:username, :password)", {"username" : username, "password" : password})

    db.commit()
    db.close()

    return render_template("create-account.html", title="Create Account")

from flask import Flask, render_template, request, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

#flask
app = Flask(__name__)
app.secret_key = 'ec40e9586e47b6594808650588668ef4920c31dd808afb8d'

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
    accounts = c.execute("SELECT * FROM logins WHERE username = :username", {"username" : username})

    for account in accounts:
        print(account[1])
        if(check_password_hash(account[1], password)):
            db.close()
            return "<h1 style='color:green'>Successfully Logged In</h1>"
    db.close()
    return render_template("incorrect-login.html")



@app.route("/register", methods=["POST"])
def register():

    db = sqlite3.connect("logins.db")
    c = db.cursor()

    username = request.form.get("username")
    password = request.form.get("password")

    c.execute("INSERT INTO logins (username, password) VALUES (:username, :password)", {"username" : username, "password" : generate_password_hash(password)})

    db.commit()
    db.close()

    return render_template("account-created.html", title="Account Created")

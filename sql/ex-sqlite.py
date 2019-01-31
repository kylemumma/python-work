import sqlite3

db = sqlite3.connect("ex-database.db")

c = db.cursor()

print("[1] Login")
print("[2] Create Account")
print()

if(input() == "1"):
    #Login
    print()
    login_u = input("Enter Username: ")
    login_p = input("Enter Password: ")

    accounts = c.execute("SELECT * FROM logins WHERE username = :user AND password = :pass", {'user' : login_u, 'pass' : login_p})

    i = 0
    accname = ""
    for acc in accounts:
        i+=1
        accname = acc[0]

    print()
    if(i == 1):
        print(f"successfully logged in {accname}")
    else:
        print("login failed")
else:
    #create Account
    print()
    new_username = input("desired username: ")
    new_password = input("desired password: ")

    c.execute("INSERT INTO logins (username, password) VALUES (:user, :pass)", {'user' : new_username, 'pass' : new_password})

    db.commit()

db.close()

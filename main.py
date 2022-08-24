# make a folder/directory with name "'templates'" and add all HTML files in it
# make a folder/directory with name "'static'" and make directory "'CSS'" in it and add all CSS, JS
# files in it
# @app.route('/subURL')     # whenever someone come on this URL woke this function
from flask import Flask, render_template, request, redirect, session
# import mysql.connector
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # 24 char random key to save on 'server' and in 'cookie'


# ######### Database connection
# conn = mysql.connector.connect(host="", user="", password="", database="")
# cursor=conn.cursor()


@app.route('/')         # root URL
def fun():
    return redirect('/login')
    # return "change in url  <br>/home <br>/login <br>/register  <br>/SecondPageURL"


@app.route('/home')
def home():     # Personal home page of user
    return render_template('home.html')

    # if 'users_id' in session:  # if already login then only show homepage
    #     return render_template('home.html')
    # else:  # else show login page
    #     return redirect('/login')


@app.route('/SecondPageURL')
def home2():
    return "By changing URL landed on   ---->   Page 2"


@app.route('/login')
def login():
    if 'users_id' not in session:  # if already not login then only load login page
        return render_template('login.html')  # Return HTML file on this URL
    else:
        return redirect('/home')


@app.route('/login_validation', methods=['POST'])
def login_validation():  # IMPORT request
    # Receiving Data from HTML **form**
    email = request.form.get("email")  # email & password in name of entry field
    passw = request.form.get("password")

    #### query run on database    # pip install mysql.connector
    # cursor.execute(f"""SELECT * FROM `TABLENAME` WHERE `EMAIL`= '{email}' and `PASSWORD`= '{passw}' """)
    # users = cursor.fetchall()       # returns list of tuples according to query

    # ######## by using if-else we can validate user
    # if len(users)==1:           # if DB gives 1 tuple
    #     session['user_id'] = users[0][0]        # primary in tuple
    return redirect('/home')
    # else:
    #     return redirect('/login')
    ############################### #function name to call whose HTML should have shown to user




#### add NEW user
@app.route('/register')
def register():
    if 'users_id' not in session:
        return render_template('register.html')
    else:
        return redirect('/home')

@app.route('/add_user', methods=['POST'])
def add_user():  # IMPORT request
    name = request.form.get("uname")  # uname, email & password are name of entry field
    email = request.form.get("email")
    passw = request.form.get("password")

    # cursor.execute(f"""INSERT INTO `TABLENAME` (`USER_ID`,`COLUMN_NAME1`, `COLUMN_NAME2`, `COLUMN_NAME3`) VALUES (NULL, '{name}', '{email}', '{passw}') """)
    # conn.commit()

    return "user Register Successfully"
    #### if we want direct login for new user  1) run a query to get user data from DB save it in tople (email is unique)
    #### set session['user_id']
    #### redirect to Home page


@app.route('/logout')
def logout():
    # session.pop('user_id')
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)

from __main__ import app, db
from flask import Flask, render_template, request, session, redirect, url_for
from flask_mysqldb import MySQL

@app.route("/login", methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = db.connection.cursor()
        cursor.execute(f"SELECT * FROM korisnik WHERE username='{username}' AND password='{password}'")
        user = cursor.fetchone()
        if user:
            session['is_logged'] = True
            session['username'] = user[1]
            session['full_name'] = user[3]
            return redirect(url_for('home'))
        message = "You entered the wrong username/password"
    return render_template("login.html", message=message)

@app.route('/logout')
def logout():
    session.pop('is_logged', None)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        full_name = request.form['full_name']
        if len(username) == 0 or len(password) == 0 or len(full_name) == 0:
            message = "All the fields are required"
        else:
            try:
                cursor = db.connection.cursor()
                cursor.execute(f"INSERT INTO korisnik VALUES (NULL,'{username}','{password}','{full_name}')")
                db.connection.commit()
                return redirect(url_for("login"))
            except:
                message = "A user with that username exists"
    return render_template("login.html",message=message)

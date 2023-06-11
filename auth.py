from __main__ import app, db
from flask import render_template, request, session, redirect, url_for

@app.route("/login", methods=['GET', 'POST'])
def login():
    if session.get("is_logged") == True:
        return redirect(url_for("home"))
    message = ""
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = db.connection.cursor()
        cursor.execute(f"SELECT * FROM korisnik WHERE korisnicko_ime='{username}' AND lozinka='{password}'")
        user = cursor.fetchone()
        cursor.close()
        if user:
            session['is_logged'] = True
            session['username'] = user[1]
            session['full_name'] = user[3]
            return redirect(url_for('home'))
        message = "Nevalidni kredencijali"
    return render_template("login.html", login_message=message)

@app.route('/logout')
def logout():
    session.pop('is_logged', None)
    session.pop('username', None)
    session.pop('full_name', None)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if session.get("is_logged") == True:
        return redirect(url_for("home"))
    message = ""
    if request.method == 'POST':
        username = request.form['username']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        if len(username) == 0 or len(password) == 0 or len(email) == 0 or len(first_name) == 0 or len(last_name) == 0:
            message = "Sva polja je neophodno ispuniti"
        else:
            try:
                cursor = db.connection.cursor()
                cursor.execute(f"INSERT INTO korisnik VALUES (NULL,'{username}','{email}','{password}','{first_name}','{last_name}',1)")
                db.connection.commit()
                cursor.close()
                return redirect(url_for("login"))
            except:
                message = "Korisnik sa tim username-om vec postoji"
    return render_template("login.html",register_message=message)

from flask import Flask, render_template, request, session, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'biblioteka'
app.secret_key = "balsa"

db = MySQL(app)

@app.route("/")
def home():
    return render_template("index.html")

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
    return render_template("register.html",message=message)

@app.route("/books")
def books():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM knjiga")
    books = cursor.fetchall()
    cursor.close()
    return render_template("books.html", books=books)

@app.route("/books/<book>/")
def single_book(book):
    if session.get("is_logged") == None or session.get("is_logged") == False:
        return redirect(url_for('login'))
    cursor = db.connection.cursor()
    cursor.execute(f"SELECT * FROM knjiga WHERE ISBN='{book}'")
    books = cursor.fetchall()
    return render_template("book.html", books=books)

if __name__ == "__main__":
    app.run(debug=True)

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

@app.route("/contact")
def contact():
    return render_template("contact.html")

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

import auth
if __name__ == "__main__":
    app.run(debug=True)

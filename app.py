from flask import Flask, render_template, abort, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'biblioteka'

app.secret_key = "df3b16da591219fc41b626eb"

db = MySQL(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/books")
def all_books():
    cursor = db.connection.cursor()
    cursor.execute("SELECT knjiga.*, autor.autor FROM knjiga JOIN autor ON knjiga.autor_id = autor.id ORDER BY knjiga.naslov")
    books = cursor.fetchall()
    cursor.close()
    return render_template("books.html", books=books)

@app.route("/books/<int:book_id>")
def single_book(book_id):
    cursor = db.connection.cursor()
    cursor.execute(f"SELECT knjiga.*, autor.autor FROM knjiga JOIN autor ON knjiga.autor_id = autor.id WHERE knjiga.id={book_id}")
    book = cursor.fetchone()
    cursor.close()
    if book:
        return render_template("book.html", book=book)
    abort(404)

@app.route("/books/add", methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        author = request.form['author']
        cover = request.form['cover']
        cursor = db.connection.cursor()
        cursor.execute(f"INSERT INTO knjiga VALUES (NULL,'{title}','{genre}',{author},'{cover}')")
        db.connection.commit()
        cursor.close()
        return redirect(url_for('all_books'))
    cursor = db.connection.cursor()
    cursor.execute(f"SELECT * FROM autor ORDER BY autor")
    authors = cursor.fetchall()
    return render_template("book_form.html", authors=authors)

import auth

if __name__ == "__main__":
    app.run(debug=True)

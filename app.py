from flask import Flask, render_template, abort, request, redirect, url_for, session
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

@app.route("/books/add", methods=['GET', 'POST'])
def add_book():
    if session.get('user_type') != 2:
        return redirect("/books")
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

@app.route("/books/edit/<int:book_id>", methods=['GET', 'POST'])
def update_book(book_id):
    if session.get('user_type') != 2:
        return redirect("/books")
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        author = request.form['author']
        cover = request.form['cover']
        cursor = db.connection.cursor()
        cursor.execute(f"UPDATE knjiga SET naslov='{title}',zanr='{genre}',autor_id={author},povez='{cover}' WHERE knjiga.id={book_id}")
        db.connection.commit()
        cursor.close()
        return redirect(url_for('all_books'))
    cursor = db.connection.cursor()
    cursor.execute(f"SELECT knjiga.*, autor.autor FROM knjiga JOIN autor ON knjiga.autor_id = autor.id WHERE knjiga.id={book_id}")
    book = cursor.fetchone()
    cursor.execute(f"SELECT * FROM autor ORDER BY autor")
    authors = cursor.fetchall()
    cursor.close()
    if book:
        return render_template("update_book.html",book=book, authors=authors)
    abort(404)

@app.route("/books/delete/<int:book_id>")
def delete_book(book_id):
    if session.get('user_type') != 2:
        return redirect("/books")
    try:
        cursor = db.connection.cursor()
        cursor.execute(f"DELETE FROM knjiga WHERE id={book_id}")
        db.connection.commit()
        cursor.close()
        return redirect("/books")
    except:
        abort(404)

@app.route("/reservations")
def all_reservations():
    if not session.get('is_logged'):
        return redirect("/login")
    if session['user_type'] == 1:
        cursor = db.connection.cursor()
        cursor.execute(f"SELECT rezervacije.id, ime, prezime, naslov, datum_preuzimanja, datum_vracanja FROM korisnik JOIN rezervacije ON rezervacije.korisnik_id = korisnik.id JOIN knjiga ON rezervacije.knjiga_id = knjiga.id WHERE korisnik.id={session['id']}  ORDER BY datum_vracanja")
        reservations = cursor.fetchall()
        cursor.close()
    else:
        cursor = db.connection.cursor()
        cursor.execute(f"SELECT rezervacije.id, ime, prezime, naslov, datum_preuzimanja, datum_vracanja FROM korisnik JOIN rezervacije ON rezervacije.korisnik_id = korisnik.id JOIN knjiga ON rezervacije.knjiga_id = knjiga.id ORDER BY datum_vracanja")
        reservations = cursor.fetchall()
        cursor.close()
    return render_template("reservations.html",reservations=reservations)

@app.route("/reservations/add",  methods=['GET', 'POST'])
def add_reservation():
    if not session.get('is_logged'):
        return redirect("/login")
    if request.method == 'POST':
        book = request.form['book']
        user = session['id']
        issue_start = request.form['issue_start']
        issue_end = request.form['issue_end']
        cursor = db.connection.cursor()
        cursor.execute(f"INSERT INTO rezervacije VALUES (NULL,{book},{user},'{issue_start}','{issue_end}')")
        db.connection.commit()
        cursor.close()
        return redirect('/reservations')
    cursor = db.connection.cursor()
    cursor.execute(f"SELECT id, naslov FROM knjiga ORDER BY naslov")
    books = cursor.fetchall()
    return render_template("reservations_form.html", books=books)

@app.route("/reservations/delete/<int:id>")
def delete_reservation(id):
    if session.get('user_type') != 2:
        return redirect("/reservations")
    try:
        cursor = db.connection.cursor()
        cursor.execute(f"DELETE FROM rezervacije WHERE id={id}")
        db.connection.commit()
        cursor.close()
        return redirect("/reservations")
    except:
        abort(404)

import auth

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/books")
def books():
    return render_template("books.html")

@app.route("/books/<book>/")
def single_book(book, name=None):
    return render_template("book.html",book=book)

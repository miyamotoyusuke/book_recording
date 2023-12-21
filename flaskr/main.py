from flaskr import app
from flask import render_template, request, session, redirect
import sqlite3
DATABASE = 'database.db'

@app.route("/", methods=["GET"])
def index():
    if 'user_id' in session:
        my_id = session["user_id"]
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute(
            "select * from book where user_id = ?", (my_id,))
        book_list = c.fetchall()
        return render_template("index.html", tpl_book_list=book_list)
    else:  
        return redirect("/login")



@app.route("/create", methods=["GET", "POST"])
def create():
    if 'user_id' in session:
        if request.method == "POST":
            user_id = session["user_id"]
            title = request.form.get("title")
            date = request.form.get("date")
            conn = sqlite3.connect("database.db")
            c = conn.cursor()
            c.execute("insert into book values(null,?,?,?)", (user_id, title, date))
            conn.commit()
            conn.close()
            return redirect("/")
        else:
            return render_template("create.html")
    else:
        return redirect("/login")

    
@app.route("/<int:id>/update", methods=["GET", "POST"])
def update(id):
    if request.method == "GET":
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute(
        "select * from book where id = ?", (id,))
        book = c.fetchone()
        return render_template("update.html", book=book)
    else:
        a = request.form.get("title")
        date = request.form.get("date")
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("update book set title= ?, date = ? where id = ?", (a, date, id))
        conn.commit()
        conn.close()
        return redirect("/")
    
@app.route("/<int:id>/delete", methods=["GET"])
def delete(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(
    "delete from book where id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")




@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute(
            "select id from user where name = ? and password = ?", (name, password))
        user_id = c.fetchone()
        conn.close()
        print(type(user_id))
        if user_id is None:
            return render_template("login.html")
        else:
            session['user_id'] = user_id[0]
            session['user_name'] = name
            return redirect("/")
    else:
        return render_template("login.html")


@app.route("/regist", methods=["GET", "POST"])
def regist():
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("insert into user values(null,?,?)", (name, password))
        conn.commit()
        conn.close()
        return redirect("/login")
    else:
        return render_template("regist.html")

# ログアウト
@app.route("/logout")
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    return redirect("/login")
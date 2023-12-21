from flask import Flask

app = Flask(__name__)
app.secret_key = 'dskfjmvdngbsnmiovenajovneov'
import flaskr.main

from flaskr import db
db.create_user_table()
db.create_book_table()
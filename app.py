import sys
sys.dont_write_bytecode = True

from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')



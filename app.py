from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    title = "Hello"
    # return render_template("index.html", title=title)
    return title

if __name__ == "__main__":
    app.debug = True
    app.run()

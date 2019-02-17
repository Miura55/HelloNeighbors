from flask import Flask, requests, jsonify, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    title = "Hello"
    return render_template("index.html", title=title)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")

from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    title = "Hello"
    return render_template("index.html", title=title)

if __name__ == "__main__":
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

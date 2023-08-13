# app.py
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, Flasker! <p>this is nice</p>"


if __name__ == "__main__":
    app.run()

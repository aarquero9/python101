from flask import Flask

app = Flask(__name__)


@app.route("/")

def hello_world():
    return "Pitxar para ir a agur <a href='/agur'>AQUI</a>"

@app.route("/agur")

def agur():
    return "Pitxar para ir a HOME <a href='/'>AQUI</a>"


if __name__ == "__main__":
    app.run()

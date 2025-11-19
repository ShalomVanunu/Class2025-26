from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1> hello class </h1>"

@app.route("/news")
def news():
    return "<h1> news data </h1>"


app.run(port=80, host="172.20.131.50")


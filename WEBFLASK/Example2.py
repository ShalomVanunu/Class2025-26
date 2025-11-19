from flask import Flask, render_template

# publish html page

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

app.run(port=80, host="172.20.131.50")


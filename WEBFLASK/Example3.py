from flask import Flask, render_template

# get data and show on page

app = Flask(__name__)

name1 = "Daria"
name2 = "Nadav"
name3 = "Brit"

@app.route("/")
def home():
    return render_template("winner_declaration.html",name1=name1,name2=name2,name3=name3)

app.run(port=80, host="172.20.131.50",debug=True)


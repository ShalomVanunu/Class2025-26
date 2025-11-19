from flask import Flask, render_template

#  show data in  html web page

app = Flask(__name__)

name1 = "Daria"
name2 = "Nadav"
name3 = "Brit"

list_of_names = [name1,name2,name3]

@app.route("/")
def home():
    return render_template("winner_declaration.html",name1=name1,name2=name2,name3=name3, nameslist =list_of_names)

app.run(port=80, host="172.20.131.50",debug=True)


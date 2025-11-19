from flask import Flask, render_template,request

# get data from html page

app = Flask(__name__)

@app.route( "/",methods= ["GET","POST"])
def home():
    if request.method =="POST":
        user = request.form['username']
        password = request.form['password']
        print(user,password)
        if password=="Password1" and user=="shalom":
            return "<h1> Good Login</h1>"
        else:
            return render_template("index.html" ,badlogin = "Wrong Password")

    else:
        return render_template("index.html")

app.run(port=80, host="172.20.131.50",debug=True)


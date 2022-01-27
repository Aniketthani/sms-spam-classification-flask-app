from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="POST":
        uname=request.form["name"]
        return f"Hello {uname}"
        
app.run(debug=True)


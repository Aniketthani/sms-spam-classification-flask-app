from flask import Flask, render_template, request
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("result.html",marks=" ")

@app.route("/show_result",methods=["POST"])
def result():
    if request.method=="POST":
        marks=request.form["marks"]
        
        
        return render_template("result.html",marks=int(marks))
    
    
app.run(debug=True)
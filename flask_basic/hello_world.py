from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

def hello_new():
    return "New Hello WOrld!"
app.add_url_rule("/hello",view_func=hello_new)

@app.route("/dynamic_url/<name>")
def dynamic_url(name):
    return f"Hello {name}"


    

app.run(debug=True)


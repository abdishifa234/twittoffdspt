#hello.py

from flask import Flask # importing class called 'Flask' from package called flask
app = Flask(__name__) #instantiating instance of the class Flask

@app.route("/")  #invoking methods/decorators
def index():
    x = 2 + 2
    return f"Hello World! {x}"


@app.route("/about")
def about():
    return "About me"



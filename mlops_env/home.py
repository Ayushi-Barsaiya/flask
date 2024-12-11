from flask import Flask

app = Flask(__name__)

# lets create end points

@app.route('/')
def home():
    return "<h3>Hello!! Welcome to Flask </h3>" 

@app.route('/ping')
def pinger():
    return"<h1>hello!!</h1>"

@app.route('/json')
def json():
    return {"key":"value"}
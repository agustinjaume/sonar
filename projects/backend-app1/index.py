from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


# env FLASK_APP=index.py flask run
# virtualenv frontend
# source frontend/Scripts/activate
# pip3 install flask
#  pip install --upgrade pip --user


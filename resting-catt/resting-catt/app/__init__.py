from flask import Flask, request
from catt.controllers import setup_cast

app = Flask(__name__)

@app.route("/")
def root():
    return {
        "msg": "Hello, there!"
    }

@app.route("/cast_site", methods=['POST'])
def cast_site():
    data = request.json
    print(data)
    if data['device'] and data['url']:
        cst = setup_cast(data['device'], 
                         controller="dashcast", 
                         action="load_url", 
                         prep="app")
        cst.load_url(data['url'])

def run():
    app.run(port=9898, host= '0.0.0.0')
from flask import Flask
import time
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def print_message():
    return "I am running on '" + os.environ['APP'] + "' app!!!"

@app.route('/healthcheck', methods=['GET'])
def print_helthcheck():
    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0')

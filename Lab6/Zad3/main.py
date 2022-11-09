from flask import Flask, escape, request
import json

app = Flask(__name__)

@app.route('/cars')
def cars():
    year = request.args.get('years')
    return ""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
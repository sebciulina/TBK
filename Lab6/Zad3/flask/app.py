import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)


def connect_db():
    return psycopg2.connect(host='172.17.0.2', database='l6z3', user='postgres', password='postgres', port=5432)

@app.route('/')
def index():
    return "<a href='/cars'>cars</a>"

@app.route('/cars', methods=['GET'])
def getCars():
    db = connect_db()
    year = request.args.get('year')

    if year is None:
        query = "SELECT * FROM Car"
    else:
        query = "SELECT * FROM Car WHERE year = " + year

    cursor = db.cursor()
    cursor.execute(query)
    output = cursor.fetchall()
    cursor.close()
    db.close()

    return jsonify(output)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
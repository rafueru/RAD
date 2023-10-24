from flask import Flask, request, jsonify, g
import sqlite3
from flasgger import Swagger

DATABASE = 'database.db'

app = Flask(__name__)
swagger = Swagger(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    conn = get_db()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS developers
                 (name TEXT, age INTEGER, city TEXT, state TEXT, phone TEXT, email TEXT,
                  experience TEXT, skills TEXT, linkedin TEXT, employment_status TEXT, salary_expectation REAL);''')

    c.execute('''INSERT INTO developers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (data['name'], data['age'], data['city'], data['state'], data['phone'], data['email'],
               data['experience'], data['skills'], data['linkedin'], data['employment_status'], data['salary_expectation']))
    conn.commit()
    return jsonify({"message": "Data received", "data": data}), 200

@app.route('/get_developers', methods=['GET'])
def get_developers():
    conn = get_db()
    c = conn.cursor()
    c.execute('''SELECT * FROM developers''')
    developers = c.fetchall()
    return jsonify({"developers": developers}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

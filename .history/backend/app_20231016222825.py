from flask import Flask, request, jsonify, g
import sqlite3

app = Flask(__name__)

DATABASE = '/database/database.db'

# Função para obter a conexão com o banco de dados
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

# Inicializar o banco de dados
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.route('/submit_developer', methods=['POST'])
def submit_developer():
    data = request.json
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        INSERT INTO developers (name, age, city, state, phone, email, experience, skills, linkedIn, employment_status, salary_expectation, other_info)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (data['name'], data['age'], data['city'], data['state'], data['phone'], data['email'], data['experience'], data['skills'], data['linkedIn'], data['employment_status'], data['salary_expectation'], data['other_info']))
    db.commit()
    return jsonify({"message": "Developer data submitted!"})

@app.route('/submit_recruiter', methods=['POST'])
def submit_recruiter():
    data = request.json
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        INSERT INTO recruiters (name, filter_city, filter_state, filter_salary, filter_area, contact, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (data['name'], data['filter_city'], data['filter_state'], data['filter_salary'], data['filter_area'], data['contact'], data['status']))
    db.commit()
    return jsonify({"message": "Recruiter data submitted!"})

@app.route('/developers', methods=['GET'])
def get_developers():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM developers')
    developers = cursor.fetchall()
    return jsonify(developers)

@app.route('/recruiters', methods=['GET'])
def get_recruiters():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM recruiters')
    recruiters = cursor.fetchall()
    return jsonify(recruiters)

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0')


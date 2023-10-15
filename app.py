from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Inicializar o banco de dados
def init_db():
    with sqlite3.connect('database.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS developers
                         (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, city TEXT, state TEXT, phone TEXT, email TEXT, experience TEXT, skills TEXT, linkedIn TEXT, employment_status TEXT, salary_expectation REAL, other_info TEXT, resume BLOB)''')
        conn.execute('''CREATE TABLE IF NOT EXISTS recruiters
                         (id INTEGER PRIMARY KEY, name TEXT, filter_city TEXT, filter_state TEXT, filter_salary REAL, filter_area TEXT, contact TEXT, status TEXT)''')
    print("Database initialized!")

init_db()

@app.route('/submit_developer', methods=['POST'])
def submit_developer():
    # Aqui, você capturaria os dados do formulário e os salvaria no banco de dados.
    # Por simplicidade, estou apenas retornando uma mensagem.
    return jsonify({"message": "Developer data submitted!"})

@app.route('/submit_recruiter', methods=['POST'])
def submit_recruiter():
    # Similar ao anterior, mas para os recrutadores.
    return jsonify({"message": "Recruiter data submitted!"})

if __name__ == '__main__':
    app.run(debug=True)

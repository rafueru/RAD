from flask import Flask, request, jsonify, g
import sqlite3

DATABASE = 'database.db'

app = Flask(__name__)

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
    # Aqui você pode adicionar o código para inserir os dados no banco de dados
    return jsonify({"message": "Data received", "data": data}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

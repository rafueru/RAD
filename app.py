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
    """
    Submit Data API
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
    responses:
      200:
        description: Data received
        schema:
          type: object
          properties:
            message:
              type: string
            data:
              type: object
    """
    data = request.json
    return jsonify({"message": "Data received", "data": data}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

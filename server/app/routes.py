from flask import jsonify
from app import app

@app.route("/", methods=['GET'])
def root():
    return jsonify({'message': 'Flask API'})

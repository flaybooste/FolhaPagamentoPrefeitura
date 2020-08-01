from flask import Flask, jsonify
from database import selecionar
import json

app = Flask("teste")
@app.route("/api")
def index():
	return jsonify(selecionar())

app.run(host='0.0.0.0',debug=True)


#!flask/bin/python
from flask import Flask, jsonify, request, abort
import json

app = Flask(__name__)

directory = [
	{
		'name' : 'Manav',
		'phone' : '2'
	},
	{
		'name' : 'Batra',
		'phone' : '1'
	}
]

@app.route('/directory', methods=['GET'])
def get():
	return jsonify({'directory': directory})

@app.route('/directory/<path:name>', methods=['GET'])
def get_number(name):
	new = [item for item in directory if item['name'] == name]
	if len(new) == 0:
		abort(404)
	return jsonify({'directory' : new[0]})

@app.route('/directory', methods=['POST'])
def post():
	directory.append(request.get_json())

	return jsonify({'directory':directory})

if __name__ == '__main__':
    app.run(debug=True)
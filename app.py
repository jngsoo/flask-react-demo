from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='client/build/static', template_folder="client/build")


@app.route('/')
def index():
    return send_from_directory(app.template_folder, 'index.html')

@app.route('/api/data')
def data():
    return jsonify([{'name': 'jeongsoo', 'age': 7}])


if __name__ == '__main__':
    app.run(use_reloader=True, port=5000, threaded=True)

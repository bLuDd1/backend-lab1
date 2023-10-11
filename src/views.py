from flask import jsonify
from src import app

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    health_status = {'status': 'OK'}
    return jsonify(health_status)

if __name__ == '__main__':
    app.run(debug=True)
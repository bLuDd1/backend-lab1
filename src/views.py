from flask import jsonify
from src import app
from datetime import datetime

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    health_status = {'status': 'OK', 'date': current_date}
    return jsonify(health_status)

if __name__ == '__main__':
    app.run(debug=True)
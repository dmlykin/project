import sys

sys.path.append('../')
sys.path.append('../..')
sys.path.append('/home/developer/project')

from flask import Flask, request, jsonify, json
from src.datamodel.fiter import Fiter

app = Flask(__name__)


@app.route('/')
def health_check():
    data = 'Hello, World!'
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/proceed_metod', methods=['GET'])
def proceed_metod():
    result = Fiter.proceed_metod()
    return app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )


@app.route('/newmodel', methods=['GET'])
def newmodel():
    result = Fiter.newmodel
    return app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=8889,
            debug=False)

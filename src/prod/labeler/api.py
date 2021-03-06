import sys

sys.path.append('../')
sys.path.append('../..')
sys.path.append('/home/developer/project')

from flask import Flask, request, jsonify, json
from src.datamodel.labelmaker import LabelMaker

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


@app.route('/proceed_metod', methods=['POST'])
def proceed_metod():
    result = LabelMaker.proceed_metod()
    return app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )


@app.route('/newmodel', methods=['GET'])
def dataset_list():
    result = LabelMaker.dataset_list
    return app.response_class(
                response=json.dumps(result),
                status=200,
                mimetype='application/json'
            )


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=8889,
            debug=False)

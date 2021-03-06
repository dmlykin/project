import sys

sys.path.append('../')
sys.path.append('../..')

import os
# import urllib
import urllib.request
from urllib.error import URLError

from flask import Flask, request, jsonify, json, send_file
from requests import HTTPError

from src.datamodel.iterpretator import Interpretator
from werkzeug.utils import secure_filename

from src.prod.utils import jpeg_bytes_io

app = Flask(__name__)


@app.route('/health_check', methods=['GET'])
def health_check():
    data = 'Hello, World!'
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/defect_stream', methods=['GET'])
def defect_stream():
    list = request.form.get('list')
    if len(list) <= 0:
        return jsonify(success=False, message="Couldn't read image"), 400
    else:
        result = Interpretator.list_interpretation(list)
        return app.response_class(
            response=json.dumps(result),
            status=200,
            mimetype='application/json'
        )




@app.route('/defect_search', methods=['GET', 'POST'])
def defect_search():
    try:
        if request.method == 'GET':
            url = request.args.get('url')
            response = urllib.request.urlopen(url)
            byte_string = response.read()
        elif request.method == 'POST':
            files = [file for _, file in request.files.items()]
            byte_string = files[0].read()

        image = Interpretator.image_interpretation(byte_string)

        return send_file(jpeg_bytes_io(image, quality=80), mimetype="image/jpeg")
    except (URLError, HTTPError):
        return jsonify(success=False, message="Couldn't read image"), 400
    except Exception as e:
        return jsonify(success=False, message=str(e), exception=e.__class__.__name__), 500


@app.route('/metrics', methods=['GET'])
def metrics():
    return Interpretator.metric()


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=8889,
            debug=False)

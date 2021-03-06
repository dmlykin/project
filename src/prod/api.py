from flask import Flask
from flask import Flask, request, jsonify, json

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

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=8889,
            debug=False)
from flask import Flask
from flask import Flask, request, jsonify, json
from flasgger import Swagger
from flasgger import swag_from


app = Flask(__name__)
swagger = Swagger(app)

path = './swdoks/health_check.yml'

@app.route('/health_check')
def health_check():
    """
    file: /src/swdoks/health_check.yml
    """
    data = 'Ok'
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
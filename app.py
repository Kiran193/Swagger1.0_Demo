
from flask import Flask, request, jsonify 
from flask_cors import CORS

from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'Secret_key'

@app.route('/')
def hello():
    return 'Hello'


SWAGGER_URL = '/swagger'
API_URL = 'http://127.0.0.1:5000/static/swagger.json'
# API_URL = 'http://clairvoyant-dev.i2econsulting.com:5000/static/swagger.json'

SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config = { 'app_name': "EWS API Documentation" } )
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


if __name__ == '__main__':
    app.run(debug=True)
    print("Running app...")

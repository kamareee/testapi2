
from flask import Flask
from flask_restful import Api

from resources.data_api import UserData

app = Flask(__name__)

app.config['DEBUG'] = True

app.secret_key = 'mysecret1'
api = Api(app)

api.add_resource(UserData, '/getParam')

if __name__ == '__main__':
    app.run(port=5001)

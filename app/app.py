# Import libraries
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app=app, prefix='/api')

app.config['JSON_SORT_KEYS'] = False



class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/', '')


if __name__ == '__main__':
    app.run(port=5000, debug=True)

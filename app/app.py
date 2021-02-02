# Import libraries
from flask import Flask
from flask_restful import Api, Resource
from drivers.mongo.mongo_driver import initialize_db
from modules.training_service.routes.sale_check_route import initialize_routes


app = Flask(__name__)

api = Api(app=app, prefix='/api')

app.config['JSON_SORT_KEYS'] = False

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/', '')

initialize_db(app)
initialize_routes(api)


if __name__ == '__main__':
    app.run(port=5000, debug=True)

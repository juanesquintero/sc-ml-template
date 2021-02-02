from flask_mongoengine import MongoEngine

mongo_db = MongoEngine()

def initialize_db(app):
    mongo_db.init_app(app)
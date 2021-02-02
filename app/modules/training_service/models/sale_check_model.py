from drivers.mongo.mongo_driver import mongo_db

class Sale_check(mongo_db.Document):
    id_user = mongo_db.StringField(required=False, Unique=False)
    id_product = mongo_db.StringField(required=False, Unique=False)
    rating = mongo_db.IntField()

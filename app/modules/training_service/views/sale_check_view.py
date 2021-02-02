from flask import Response, request
from modules.training_service.models import sale_check_model

from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, \
    ValidationError
from errors import SchemaValidationError, \
    InternalServerError

class TrainingApi(Resource):
    def get():
        all_sale_checks = sale_check.Objects.json()
        return Response(all_sale_checks, mimetype="application/json", status=200)
    def post():
        try:                  
            body = request.get_json()
            new_sale = sale_check(**body).save()
            id = sale_check.id
            return {'id': str(id)},200
        except (FieldDoesNotExist, ValidationError):
            raise (SchemaValidationError)
        except Exception as e:
            raise InternalServerError


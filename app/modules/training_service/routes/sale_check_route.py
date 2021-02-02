from modules.training_service.views.sale_check_view import TrainingApi

def initialize_routes(api):
    api.add_resource(TrainingApi, '/api/sales')
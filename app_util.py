from routes.capability import capability_endpoint
from routes.resource import resource_endpoint
from routes.scope_endpoint import scope_endpoint
from routes.future_capabilities_endpoint import future_capabilities_endpoint

# Handles basic app functions
class App_Util:

    # Registers all the blueprints for all the routes onto the app passed
    @staticmethod
    def register_blueprints(app):
        app.register_blueprint(capability_endpoint)
        app.register_blueprint(resource_endpoint)
        app.register_blueprint(scope_endpoint)
        app.register_blueprint(future_capabilities_endpoint)
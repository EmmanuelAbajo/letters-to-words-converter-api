from flask import Flask

def create_app():
    app = Flask(__name__)

    from .api import bp as apiv1_blueprint

    app.register_blueprint(apiv1_blueprint,url_prefix='/api/v1')
    
    return app
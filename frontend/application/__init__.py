import os

from flask import Flask, Blueprint
from flask_restful import Api
import logging
# from application.api import v0


def create_app() -> Flask:
    PROJECT_NAME = os.path.dirname(os.path.abspath(__file__))  # DataDiscovery/frontend/application

    logging.basicConfig(filename=os.path.join(PROJECT_NAME, 'logs', 'application.log'),
                        format= '%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s',
                        level=logging.DEBUG,
                        datefmt='%Y-%m-%d %H:%M:%S'
                        )
    logging.info('Starting application')

    api_bp = Blueprint('api', __name__, url_prefix='/api')
    api = Api(api_bp)




    app = Flask(__name__, instance_relative_config=True)

    return app

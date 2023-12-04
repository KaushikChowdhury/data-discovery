from flask import Blueprint

blueprint = Blueprint('main', __name__, url_prefix='/api/')

print(__name__)
import logging
from flask.blueprints import Blueprint

LOGGER = logging.getLogger(__name__)

log_blueprint = Blueprint('log', __name__, url_prefix='/log/')

@log_blueprint.route('/v0', methods=['GET'])
def get_log():
    LOGGER.info('get_log()')
    return 'get_log()'
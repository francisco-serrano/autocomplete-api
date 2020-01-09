from flask import jsonify, Blueprint

from controllers.dependencies import dependencies

health = Blueprint('health', __name__)
autocompleter = dependencies['autocompleter']


@health.route('/health')
def health_check():
    return jsonify({'response': autocompleter.health_check()})

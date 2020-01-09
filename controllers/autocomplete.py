import time

from flask import jsonify, Blueprint, request

from controllers.dependencies import dependencies
from utils.logger import logger

autocomplete = Blueprint('autocomplete', __name__)
autocompleter = dependencies['autocompleter']


@autocomplete.route('/autocomplete')
def autocomplete_query():
    """ Generate autocompletions given the query 'q' """
    start = time.time()
    q = request.args.get('q')
    completions = autocompleter.generate_completions(q)
    logger.info('elapsed time: {}'.format(time.time() - start))
    return jsonify({"Completions": completions})

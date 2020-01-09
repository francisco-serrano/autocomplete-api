""" Template for autocomplete server, you probably won't need to edit anything
in this file. """

from flask import Flask, request, jsonify
from services import autocompleter
from utils.logger import logger

import time

app = Flask(__name__)
my_autocompleter = autocompleter.Autocompleter()


@app.route('/autocomplete')
def autocomplete():
    """ Generate autocompletions given the query 'q' """
    start = time.time()
    q = request.args.get('q')
    completions = my_autocompleter.generate_completions(q)
    logger.info('elapsed time: {}'.format(time.time() - start))
    return jsonify({"Completions": completions})


if __name__ == "__main__":
    app.run(host='0.0.0.0')

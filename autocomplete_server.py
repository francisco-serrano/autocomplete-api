""" Template for autocomplete server, you probably won't need to edit anything
in this file. """

from flask import Flask, request, jsonify
from core import autocompleter
from utils.logger import logger

import time

app = Flask(__name__)
autocompleter = autocompleter.Autocompleter()


@app.route('/autocomplete')
def autocomplete():
    """ Generate autocompletions given the query 'q' """
    start = time.time()
    q = request.args.get('q')
    completions = autocompleter.generate_completions(q)
    logger.info('elapsed time: {}'.format(time.time() - start))
    return jsonify({"Completions": completions})


@app.route('/health')
def health():
    return jsonify({'response': autocompleter.health_check()})


if __name__ == "__main__":
    app.run(host='0.0.0.0')

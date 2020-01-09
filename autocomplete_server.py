""" Template for autocomplete server, you probably won't need to edit anything
in this file. """

from flask import Flask

from controllers.health import health
from controllers.autocomplete import autocomplete

app = Flask(__name__)
app.register_blueprint(health)
app.register_blueprint(autocomplete)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

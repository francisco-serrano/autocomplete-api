import json
import pickle

DEFAULT_FILENAME = "autocompleter.pkl"


class Autocompleter:
    def __init__(self):
        pass

    def import_json(self, json_filename):
        pass

    def generate_completions(self, prefix_string):
        return []

    def save(self, filename=DEFAULT_FILENAME):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def load(cls, filename=DEFAULT_FILENAME):
        with open(filename, "rb") as f:
            return pickle.load(f)

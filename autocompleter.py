from elasticsearch import Elasticsearch, helpers
import pickle
from parse_json import generate_elastic_search_input

DEFAULT_FILENAME = "autocompleter.pkl"


class Autocompleter:
    def __init__(self):
        self.es = Elasticsearch()
        self.es.indices.delete(index='challenge')
        self.es.indices.create(index='challenge', body={
            'mappings': {'properties': {'message': {'type': 'search_as_you_type'}}}
        })

    def import_json(self, json_filename):
        helpers.bulk(self.es, generate_elastic_search_input(json_filename))

    def generate_completions(self, prefix_string):
        return []

    def save(self, filename=DEFAULT_FILENAME):
        pass
        # with open(filename, "wb") as f:
        #     pickle.dump(self, f)

    @classmethod
    def load(cls, filename=DEFAULT_FILENAME):
        with open(filename, "rb") as f:
            return pickle.load(f)

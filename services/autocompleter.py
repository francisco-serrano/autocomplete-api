import json
import string
import os

from functools import reduce
from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Search, Q
from utils.logger import logger

DEFAULT_FILENAME = os.getenv('BASE_JSON_DIR', './sample_conversations.json')

INDEX_NAME = 'challenge'
INDEX_SETTINGS = {
    'mappings': {'properties': {'message': {'type': 'search_as_you_type'}}}
}

ELASTICSEARCH_HOST = os.getenv('ELASTICSEARCH_HOST', 'localhost')
ELASTICSEARCH_PORT = int(os.getenv('ELASTICSEARCH_PORT', '9200'))


def generate_elastic_search_input(json_input):
    input_file = open(json_input, encoding='utf-8')
    data = json.load(input_file)

    logger.info('{} opened successfully'.format(json_input))

    issues = data['Issues']

    messages = list(map(lambda x: x['Messages'], issues))
    messages = reduce(list.__add__, messages)
    messages = list(map(lambda x: x['Text'], messages))
    messages = list(map(lambda x: x.translate(str.maketrans('', '', string.punctuation)), messages))
    messages = set(messages)

    indexes = list(range(0, len(messages)))

    logger.info('{} successfully parsed, amount of messages: {}'.format(json_input, len(messages)))

    for idx, msg in zip(indexes, messages):
        yield {
            '_index': 'challenge',
            '_id': idx,
            '_source': {
                'message': msg
            }
        }


class Autocompleter:
    def __init__(self):
        self.es = Elasticsearch([{'host': ELASTICSEARCH_HOST, 'port': ELASTICSEARCH_PORT}])
        self.search = Search(using=self.es, index=INDEX_NAME)

    def import_json(self, json_filename=DEFAULT_FILENAME):
        self.es.indices.delete(index=INDEX_NAME, ignore_unavailable=True)
        self.es.indices.create(index=INDEX_NAME, body=INDEX_SETTINGS)
        helpers.bulk(self.es, generate_elastic_search_input(json_filename))
        logger.info('Bulk Insert from JSON successful')

    def generate_completions(self, prefix_string):
        logger.info('searching completions for {}'.format(prefix_string))

        q = Q('multi_match',
              query=prefix_string,
              fields=['message', 'message._2gram', 'message._3gram'],
              type='bool_prefix'
              )

        response = self.search.query(q).execute()
        response = list(map(lambda x: x['message'], response))

        logger.info('{} completions found'.format(len(response)))

        return response

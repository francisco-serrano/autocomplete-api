from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Search, Q

from utils.logger import logger
from environment import environment
from utils.json_parser import generate_elastic_search_input


INDEX_NAME = 'challenge'
INDEX_SETTINGS = {
    'mappings': {'properties': {'message': {'type': 'search_as_you_type'}}}
}

INPUT_JSON = environment['input_json']
ELASTICSEARCH_HOST = environment['es_host']
ELASTICSEARCH_PORT = environment['es_port']


class Autocompleter:
    def __init__(self):
        self.es = Elasticsearch(
            [{'host': ELASTICSEARCH_HOST, 'port': ELASTICSEARCH_PORT}],
            timeout=20, max_retries=3
        )
        self.search = Search(using=self.es, index=INDEX_NAME)

    def health_check(self):
        return self.es.cluster.health()

    def import_json(self, json_filename=INPUT_JSON):
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

import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

environment = {
    'es_host': os.getenv('ELASTICSEARCH_HOST', 'localhost'),
    'es_port': int(os.getenv('ELASTICSEARCH_PORT', '9200')),
    'input_json': os.getenv('BASE_JSON_DIR', os.path.join(ROOT_DIR, 'sample_conversations.json'))
}

import os

environment = {
    'es_host': os.getenv('ELASTICSEARCH_HOST', 'localhost'),
    'es_port': int(os.getenv('ELASTICSEARCH_PORT', '9200')),
    'input_json': os.getenv('BASE_JSON_DIR', '../sample_conversations.json')
}

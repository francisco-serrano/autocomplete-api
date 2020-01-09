import json
import string

from functools import reduce

from utils.logger import logger


def generate_elastic_search_input(json_input):
    issues = load_base_json(json_input)

    messages = parse_messages(issues)

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


def load_base_json(json_file):
    input_file = open(json_file, encoding='utf-8')
    data = json.load(input_file)

    logger.info('{} opened successfully'.format(json_file))

    return data['Issues']


def parse_messages(issues):
    messages = list(map(lambda x: x['Messages'], issues))
    messages = reduce(list.__add__, messages)
    messages = list(map(lambda x: x['Text'], messages))
    messages = list(map(lambda x: x.translate(str.maketrans('', '', string.punctuation)), messages))
    messages = list(filter(lambda x: len(x) != 0, messages))
    messages = set(messages)

    return messages

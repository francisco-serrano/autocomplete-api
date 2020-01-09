import json
import string
from functools import reduce
from elasticsearch import Elasticsearch, helpers

# def generate_idx(amount):
#     for i in range(amount):
#         yield i


# def generate_elastic_search_input(json_input, json_output):
# def generate_elastic_search_input(json_input):
#     input_file = open(json_input, encoding='utf-8')
#     data = json.load(input_file)
#
#     issues = data['Issues']
#
#     messages = list(map(lambda x: x['Messages'], issues))
#     messages = reduce(list.__add__, messages)
#     messages = list(map(lambda x: x['Text'], messages))
#     messages = list(map(lambda x: x.translate(str.maketrans('', '', string.punctuation)), messages))
#     messages = set(messages)
#     # messages = list(map(lambda x: {'message': x}, messages))
#     # messages = list(map(lambda x: json.dumps(x), messages))
#
#     # indexes = list(map(lambda x: {'index': {'_id': obtain_idx()}}, messages))
#     # indexes = list(map(lambda x: {'index': {'_id': x}}, generate_idx(len(messages))))
#     # indexes = list(map(lambda x: json.dumps(x), indexes))
#     indexes = list(range(0, len(messages)))
#
#     for idx, msg in zip(indexes, messages):
#         yield {
#             '_index': 'challenge',
#             '_id': idx,
#             '_source': {
#                 'message': msg
#             }
#         }
    # zipped = list(zip(indexes, messages))
    # zipped = list(map(lambda x: '\n'.join(x), zipped))
    # zipped = '\n'.join(zipped)


    # output_file = open(json_output, mode='w', encoding='utf-8')
    # output_file.write(zipped + '\n')
    # output_file.close()


# generate_elastic_search_input('./sample_conversations.json', 'target_messages.json')
# es = Elasticsearch()
# helpers.bulk(es, generate_elastic_search_input())

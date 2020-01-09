## Autocomplete Service

### Steps
At the moment we only have dev environment for local development
1. Launch ElasticSearch cluster with commands inside `launch-elasticsearch.sh`
2. Launch container with commands inside `run-outside.sh`
3. Once inside the container: use `Makefile`  

Make sure ElasticSearch index is effectively populated (`make build`) before running the API
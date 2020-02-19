Elasticsearch:

RAM consumption previous to elasticsearch start -> 198 Mb
RAM consumption after starting elasticsearch -> 770 Mb

Parameters used on container:

Env vars:

- ES_JAVA_OPTS=-Xms256m -Xmx256m -> For JAVA HEAP mem
- discovery.type=single-node -> For running single cluster node mode

Final Docker run command for testing purposes:

docker run -d --rm -p 9200:9200 -p 9300:9300 -e "ES_JAVA_OPTS=-Xms256m -Xmx256m" -e "discovery.type=single-node" elasticsearch:7.5.1

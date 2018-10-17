#!/bin/env python
###
# Skript um ids aus der localen es-instanz in txt zu schreiben
# ETH Library: Sven Koesling
# Oktober 2018
import sys
from elasticsearch import Elasticsearch

es = Elasticsearch()
index = sys.argv[1]

res = es.search(index=index, filter_path=['hits.hits._source.orig_id'], body={"query": {"match_all": {}}, 'size': 100})
print("Es wurden ", len(res["hits"]["hits"]), " Treffer gefunden.")

for hit in res["hits"]["hits"]:
    '''irgendein comment '''
    print(hit['_source']['orig_id'])

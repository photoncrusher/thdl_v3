from elasticsearch import Elasticsearch, helpers
import pandas as pd
import time
import csv
from collections import deque
from elasticsearch.helpers import bulk, parallel_bulk
es = Elasticsearch("https://elastic:2mbN3LeoKyhLtS1JIF0WASZW@i-o-optimized-deployment-5033c8.es.eastus2.azure.elastic-cloud.com:9243")

f = open("E:\Working place\PROJECT 20202\AAATEST\\new_crawler\\new_crawler\data.csv",encoding='utf-8')
df = csv.DictReader(f)
es_idx = 'apple'
actions = []
for data in df:
    action = {
        "_index": es_idx,
        "_type": "product",
        "_source": data
    }
    actions.append(action)
    if len(actions) >= 100:
        deque(parallel_bulk(es, actions), maxlen=0)
        actions = []
    time.sleep(.01)
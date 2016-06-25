#!/bin/python

from flask import Flask, Response, request
import redis
import json
from memcached_stats import MemcachedStats
import config

app = Flask(__name__)


@app.route("/cache-stats")
def cache_stats():
    config_name = request.args.get('name')
    cache_config = config.get(config_name)
    if cache_config is None:
        return Response({}, 404, content_type='application/json')

    if cache_config['type'] == 'redis':
        r = redis.StrictRedis(host=cache_config['host'], port=cache_config['port'], db=0)
        return Response(json_to_html(r.info()), 200, content_type='application/json')
    elif cache_config['type'] == 'memcached':
        cache = MemcachedStats(cache_config['host'], cache_config['port'])
        return Response(json_to_html(cache.stats()), 200, content_type='application/json')


@app.route("/cache-services", methods=['POST'])
def register_cache_services():
    return "Hello World!"


@app.route("/cache-services", methods=['DELETE'])
def unregister_cache_services():
    return "Hello World!"


def json_to_html(json_object):
    html = "<pre>\n"
    for (key, val) in json_object.items():
        html += key + ":" + repr(val) + "\n"
    html += "</pre>"
    return html


if __name__ == "__main__":
    app.run()

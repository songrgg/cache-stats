import os

from flask import json


def get(name):
    root = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(root, "config", "cache-services.json")
    data = json.load(open(json_url))
    for ele in data:
        if ele['name'] == name:
            return ele
    return None


def add(obj):
    json_obj = get()
    json_obj.add(obj)
    root = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(root, "config", "cache-services-template.json")
    open(json_url).write(json.dumps(json_obj))


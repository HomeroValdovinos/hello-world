# -*- coding: utf-8 -*-
import json

json_file = open('marvel.json'.read()
json_data = json.loads(json_file)

print json_data['data']


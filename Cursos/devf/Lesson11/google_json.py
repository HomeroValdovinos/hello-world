# Encoding
# -*- coding: utf-8 -*-

import requests
import json

url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&type=restaurant&keyword=cruise&key=AIzaSyBSa0SUjt7GVytZzWuzp32_nbby0RNBoNE"
open_file = requests.get(url)
allresults = open_file.json()
# results = allresults["results"][0]['opening_hours']['open_now']
results = allresults["results"][0]
print results

class AllResults(object):
    def __init__(self, all_results):
        self.all_results = all_results

    def get_results(self):
        return Results(self.all_results)

class Results(object):
    def __init__(self, results):
        self.results = results

# json_file = open('marvel.json').read()
# json_data = json.loads(json_file)
# data = TheData(json_data['data'])
#
#
# class TheData(object):
#     def __init__(self, data_object):
#         self.data = data_object
#         self.limit = data_object['limit']
#         self.total = data_object['total']
#         self.count = data_object['count']
#         self.results = data_object['results']
#
#     def get_results(self):
#         return Results(self.results)



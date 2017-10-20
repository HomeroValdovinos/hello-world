# Encoding
# -*- coding: utf-8 -*-

import requests


class TasteDive(object):
    def __init__(self):
        query = 'Game of Thrones'
        parameters = {'k': '287946-Test-90NR5BYV', 'q': query}
        url = 'http://tastedive.com/api/similar?'
        response = requests.get(url, params=parameters)
        data = response.json()
        Info(data["Similar"]["Info"])
        Results(data["Similar"]["Results"])


class Info(object):
    type_search = []
    type_name = []

    def __init__(self, info):
        self.info = info
        for x in range(len(self.info)):
            self.type_search.append(self.info[x]["Type"])
            self.type_name.append(self.info[x]["Name"])

    def get_info(self):
        return self.type_search, self.type_name


class Results(object):
    type_results = []
    name_results = []

    def __init__(self, results):
        self.results = results
        for x in range(len(self.results)):
            # self.type_results.append(self.results[x]["Type"])
            # self.name_results.append(self.results[x]["Name"])
            self.type_results = self.results[x]["Type"]
            self.name_results = self.results[x]["Name"]
            print "The relations are:", self.type_results, "and the name is:", self.name_results


TasteDive()


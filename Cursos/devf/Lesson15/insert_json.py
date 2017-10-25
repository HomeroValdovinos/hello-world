import requests


class TasteDive(object):
    def __init__(self):
        query = 'Game of Thrones'
        parameters = {'k': '287946-Test-90NR5BYV', 'q': query}
        url = 'http://tastedive.com/api/similar?'
        response = requests.get(url, params=parameters)
        data = response.json()
        Results(data["Similar"]["Results"])


class Results(object):
    def __init__(self, results):
        self.results = results
        for x in range(len(self.results)):
            for y in range(len(self.results[x]["Name"])):
                print("Entro al segundo for")
                print("y esto traeeeeeeee", self.results[x]["Name"])
                if self.results[x]["Name"] == "Da Vinci's Demons":
                    print("HOMERO", self.results[x]["Name"])
            # if self.results[x]["Name"] == "Da Vinci's Demons":
            #     break
            # else:
            name_search = self.results[x]["Name"]
            type_search = self.results[x]["Type"]
            InsertResult(name_search, type_search)


class InsertResult(object):
    def __init__(self, name_search, type_search):
        self.name_search = name_search
        self.type_search = type_search
        print(self.name_search)
        print(self.type_search)


TasteDive()


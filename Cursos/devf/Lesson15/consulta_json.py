import requests
import psycopg2


class TasteDive(object):
    def __init__(self):
        query = 'Game of thrones'
        parameters = {'k': '287946-Test-90NR5BYV', 'q': query}
        url = 'http://tastedive.com/api/similar?'
        response = requests.get(url, params=parameters)
        json_object_response = response.json()
        search = Search(json_object_response)
        connection = psycopg2.connect("dbname=cinta_roja_test user=postgres password=12345")
        cur = connection.cursor()
        for x in range(len(search.results)):
            # list_new = []
            value1 = search.results[x]["Name"]
            value2 = search.results[x]["Type"]
            # for y in range(len(value1)):
            #     if value1[y] == "'":
            #         for z in range(len(value1)):
            #             if value1[z] != "'":
            #                 list_new.append(value1[z])
            #         value1 = list_new
            insert_table = """
            INSERT INTO info_tastedive
            VALUES ('{}', '{}');
            """.format(value1, value2)
            cur.execute(insert_table)
            connection.commit()
        cur.close()
        connection.close()
        print search.results


class Search(object):
    def __init__(self, data_object):
        self.data = data_object
        self.similar = self.data['Similar']
        self.info = self.similar['Info']
        self.results = self.similar['Results']


TasteDive()


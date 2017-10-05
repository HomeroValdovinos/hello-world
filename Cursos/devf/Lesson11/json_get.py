#Encoding
# -*- coding: utf-8 -*-
import requests


class main_init(object):
    def __init__(self):
        latitud = float(raw_input("¿Favor de escribir latitud?"))
        longitud = float(raw_input("¿Favor de escribir longiutd?"))
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+str(latitud)+","+str(longitud)+"&radius=500&type=restaurant&keyword=cruise&key=AIzaSyBSa0SUjt7GVytZzWuzp32_nbby0RNBoNE"
        response = requests.get(url)
        data = response.json()
        resultsall = data["results"]
        results(resultsall)


class results(object):
        lista = []

        def __init__(self, response):
           self.results = response
           for x in range(len(self.results)):
                self.lista.append(self.results[x])
           photos(self.lista)

class photos(object):
    list_new = []
    def __init__(self, photos):
        self.photo = photos
        for x in range(len(self.photo)):
            self.list_new.append(self.photo[x]['geometry'])
        location(self.list_new)


class location(object):
    lista_location = []
    def __init__(self, lugar):
        self.lugar = lugar
        for x in range(len(self.lugar)):
            self.lista_location.append(self.lugar[x]['location'])
        geolocalizacin(self.lista_location)

class geolocalizacin(object):
    lista_lat = []
    lista_lon = []

    def __init__(self, geo):
        self.geolocali = geo
        for i in range(len(self.geolocali)):
            print str(self.geolocali[i]['lat']) + ',' + str(self.geolocali[i]['lng'])


#-33.8670522
#151.1957362
main_init()
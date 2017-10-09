# Encoding
# -*- coding: utf-8 -*-

import requests


# latitud = float(raw_input("¿Favor de escribir latitud?"))
# longitud = float(raw_input("¿Favor de escribir longiutd?"))
latitud = -33.8670522
longitud = 151.1957362
url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(latitud) + "," + str(longitud) + "&radius=500&type=restaurant&keyword=cruise&key=AIzaSyBSa0SUjt7GVytZzWuzp32_nbby0RNBoNE"
response = requests.get(url)
data = response.json()
resultsall = data["results"]
print "esto trae result all", resultsall

# -*- coding: utf-8 -*-

import os
path = "C:/prank/"
path_new = "C:/prank/new"
lista_de_archivos = os.listdir(path)
print(lista_de_archivos)
avoid_numbers = "1,2,3,4,5,6,7,8,9,0"


for x in lista_de_archivos:
    nuevo = x.translate(None, avoid_numbers)
    # os.chdir("C:/prank/new")
    os.rename(path+x,path_new+nuevo)
    # print nuevo




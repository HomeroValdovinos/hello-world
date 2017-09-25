# -*- coding: utf-8 -*-

#validar elementos de una IP
#validar elementos sean solo números
#validar elementos no sean mayores a tres dígitos

ip=raw_input("Cual es tu IP: ")
print ip
lista=[]
#123.456.789.123
for i in range(len(ip)):
    print ip[i]
    if (ip[i] != '.' || ip[i].isdigit()):
            lista.append(ip[i])
print " La lista creada es: ", lista
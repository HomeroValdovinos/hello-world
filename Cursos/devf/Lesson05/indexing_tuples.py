# -*- coding: utf-8 -*-

def indexing_tuplas():
    n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
    print "Esto trae n_tuple", n_tuple
    print(n_tuple[1][2])


indexing_tuplas()


def cambiando_elementos():
    my_tuple = (4, 2, 3, [6, 5])
    my_tuple[3][0] = 9 # Con esto cambiamos el valor la posicion 3 ([6,5]), en especifico el valor 0 (6) y se cambia a 9
    print (my_tuple)
    # my_tuple[1] = 9 #Esto no se puede, porque tuple no soporta la asignación de elmentos


cambiando_elementos()


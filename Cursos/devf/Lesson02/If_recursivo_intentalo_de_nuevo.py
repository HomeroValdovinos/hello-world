# -*- coding: utf-8 -*-
def play(intento=1):
    respuesta = raw_input("¿De que color es una naranja?\n")
    if respuesta != "naranja":
        if intento < 3:
            print "\nFallaste! Intentálo de nuevo"
            intento +=1
            play(intento) #Llamada recursiva
        else:
            print "\nPerdiste!!"
    else:
        print "\nGanaste!"

play()

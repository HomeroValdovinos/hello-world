hora = []
hora_nueva=[]
hora_final=[]
hora_final2=[]
hora= raw_input("Ingresa la hora en 24hrs: ")

for i in range(len(hora)):
    # print hora[i]
    if hora[i] != ':':
            hora_nueva.append(hora[i])

    if len(hora_nueva) >= 4:
        print "la cadena es mayor o igual a 4"
        hora_inicial = hora_nueva[0]+hora_nueva[1]
        hora_inicial2= hora_nueva[2]+hora_nueva[2]
        horatotal= int(hora_inicial) - 12
        print horatotal
        horatotal2 = int(hora_inicial2)
        print horatotal, ":", horatotal2
    elif len(hora_nueva) == 3:
        # hora_final = hora_nueva[0], ":" hora_nueva[1],hora_nueva[2]
        hora_final=hora
        print "La hora es: ", hora_final
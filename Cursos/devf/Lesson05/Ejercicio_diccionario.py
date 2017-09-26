# def creating_list(counter=1):
#     size_string = int(input("Which is the size of the string? \n"))
#     if size_string <= 1:
#         if counter < 3:
#             print "\nThe string shouldn't be major than 0. Please try again!!!!"
#             counter += 1
#             creating_list(counter)
#         else:
#             print "\nINVALID INFORMATION...BYE!!"
#     else:
#         nombre_familia(size_string)

def nombre_familia():
    directorio={}
    for x in range(4):
        directorio[x] = raw_input(input("Ingresa la cadena: "))
        print x
    print (directorio)

nombre_familia()
#
#     dict1 = {1: 'moises', 2: 'eva', 3: 'homero'}
#     print dict1
#
# nombre_familia()
#
#

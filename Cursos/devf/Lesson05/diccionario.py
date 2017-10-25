# def crear_diccionario():
#     my_dict = {1: 'apple', 2: 'ball'}
#     print (my_dict)
#
#     my_dict2 = {'name': 'John', 1:[2, 4, 3]}
#     print my_dict2
#
#     my_dict3= dict({1: 'apple', 2: 'ball'})
#     print my_dict3
#
#     my_dict4= dict([(1, 'apple'), (2, 'ball')])
#     print my_dict4
#
# crear_diccionario()
#
# def accesar_elementos():
#     my_dict5 = {'name': 'Jack', 'age': 26, 'address': 'Amado Nervo'}
#     print (my_dict5['name'])
#     print (my_dict5.get())
#     print (my_dict5['address'])
#
# accesar_elementos()
#
def cambiar_agregarelementnos():
    my_dict6 = {'name': 'hugo', 'age': 26}
    print "First time", (my_dict6)
    my_dict6['age'] = 32
    print (my_dict6)
    my_dict6['address']='zapopan'
    print my_dict6

    my_dict6['nombre'] = my_dict6['name']
    del my_dict6['name']
    print(my_dict6)

cambiar_agregarelementnos()

# def eliminar_elementos():
#     squares = {1:1, 2:4, 3:9, 4:16, 5:25}
#     print (squares)
#     print (squares.pop(4))
#     print (squares)
#
#     print(squares.popitem())
#     print (squares)
#
#     del squares[5]
#     print (squares)
#
#     squares.clear()
#     print (squares)
#
# eliminar_elementos()


# def ejercicio():
#     squares2 = {x: x*x for x in range(6)}
#     print (squares2)
#
#     # equivalentes
#     squares3 = {}
#     for y in range(6):
#         squares3[y] = y*y
#     print (squares3)
#
# ejercicio()
#
#
# lista = [1,2,3,4]
# sett = {1,2,3}
# tup  = (1,2,3)
# dic = {1:'value', 2:'value2', 3:'value3'}


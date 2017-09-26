set_enteros = {1, 3}
print(set_enteros)

#Dos propiedades, variables multables, que pueden cambiar y las inmutables, como variables

# set_enteros = {1, 2, 5, 3, 'hola', 3, 4, 'hola', 3}
# print(set_enteros)
#
# set_enteros.add(6)
# print(set_enteros)

set_enteros.update([4, 5], {1,6,8})
print(set_enteros)

set_enteros.discard(9)
print(set_enteros)

my_set = set("Hola Mundo")
print my_set.pop()


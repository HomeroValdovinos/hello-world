class Television():

    iva = 1.16
    numero_de_television = 0

    def __init__(self, marca, modelo, tamanio, precio, tienda, precioiva):
        self.marca = marca
        self.modelo = modelo
        self.tamanio = tamanio
        self.precio = precio
        self.tienda = tienda
        self.precioiva = precio * Television.iva

        Television.numero_de_television += 1
    def tamanio_tv(self):
        return self.tamanio

    def marca_tv(self):
        return self.marca

    # def aplicar_iva(self):
    #     precioiva = (self.precio * self.iva)
    #     return precioiva

    # def aplicar_iva(self):
    #     self.precioiva = (self.precioiva * self.iva)


television_1 = Television("Sony", "VAIO", "55", 10000, "BestBuy", 10000)
television_2 = Television("Samsung", "Smart7", "55", 12000, "Liverpool", 12000)

print television_1.__dict__


# print television_1.precio
# television_1.aplicar_iva()
# print television_1.__dict__
#
# print Television.numero_de_television
# print television_1.aplicar_iva()
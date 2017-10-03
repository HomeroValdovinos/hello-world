class Television():

    iva = 1.16
    numero_de_television = 0

    def __init__(self, marca, modelo, tamanio, precio, tienda):
        self.marca = marca
        self.modelo = modelo
        self.tamanio = tamanio
        self.precio = precio
        self.tienda = tienda

        Television.numero_de_television += 1
    def tamanio_tv(self):
        return self.tamanio

    def marca_tv(self):
        return self.marca

    def aplicar_iva(self):
        self.precio = (self.precio * self.iva)


television_1 = Television("Sony", "VAIO", "55", 10000, "BestBuy")
television_2 = Television("Samsung", "Smart7", "55", 12000, "Liverpool")

print television_1.__dict__
print television_1.precio
television_1.aplicar_iva()
print television_1.__dict__

print "El Numero de televisiones es:", Television.numero_de_television

class Empleado:
    # variable de clase
    # constantes para todas las instancias

    monto_para_aumento = 1.04
    numero_de_empleados = 0

    #Metodo init ca a correr automaticamente cada que creamos una nueva instancia
    def __init__(self, nombre, apellido, salario):
        # self -> current instance
        self.nombre = nombre
        self.apellido = apellido
        self.email = nombre + "." + apellido + "@company.com"
        self.salario = salario

        Empleado.numero_de_empleados += 1

    #No olvidar escribir self cada que definamos un nuevo metodo
    def nombre_completo(self):
        return '{} {}'.format(self.nombre, self.apellido)

    def obtnener_salario(self):
        return self.salario

    def aplicar_salario(self):
        self.salario = int(self.salario * self.monto_para_aumento)

# print Empleado.numero_de_empleados


developer = Empleado("Homero", "Valdovinos", 30000)

qa_tester = Empleado("roberto", "diaz", 10000)

print developer
print qa_tester

print developer.__dict__




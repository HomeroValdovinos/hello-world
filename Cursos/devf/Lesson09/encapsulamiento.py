class Persona:

    def __init__(self, nombre, email, age):
        self.nombre = nombre
        self.__email = email
        self.__age = age

    def update_email(self, new_email):
        self.email = new_email

    def email(self):
        return self.__email

    def __show_age(self):
        return self.__age

    def show_age(self):
        return self.__get_age()

    def __get_age(self):
        return self.__age

    def update_email(self, new_email, algo_mas):
        self.__email = new_email + algo_mas


tk = Persona("TK", "tk@gmail.com", 25)
# print tk.email()
print tk.__dict__
#
tk.update_email("hola@gmail.com")
print tk.__dict__


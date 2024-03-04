# class Madre:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

#     def deportes(self):
#         print("Me gusta hacer deportes")

#     def cocinar(self):
#         print("Me gusta cocinar mucho")


# class Padre:
#     def __init__(self, ojos):
#         self.ojos = ojos

#     def cocinar(self):
#         print("Me gusta cocinar")


# class hijx(Madre, Padre):

#     def __init__(self, nombre, edad, ojos, estudios):
#         Madre.__init__(self, nombre, edad)
#         Padre.__init__(self, ojos)
#         self.estudios = estudios

#     def estudiar(self):
#         print("Estudio mucho")


# garazi = hijx("Garazi", 20, "Azules", "Programación")

# print(garazi.nombre)
# print(garazi.edad)
# print(garazi.ojos)
# print(garazi.estudios)


class Direccion:
    def __init__(self, calle, ciudad):
        self.calle = calle
        self.ciudad = ciudad

    def mostrar(self):
        print(self.calle)
        print(self.ciudad)


class Persona:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def mostrar(self):
        print(self.nombre + " " + self.email)


# Agregar funcionalidad para usar la herencia múltiple
class Contacto(Persona, Direccion):
    def __init__(self, calle, ciudad, nombre, email, active):
        Direccion.__init__(self, calle, ciudad)
        Persona.__init__(self, nombre, email)
        self.active = active


# Instanciar un contacto que es activo (True)
jon = Contacto("Jon", "tugrp@example.com", "Calle 1", "Ciudad 1", True)

jon.mostrar()
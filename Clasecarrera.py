class Carrera(object):
    __codigo=0
    __nombre=""
    __tipo=""
    __duracion=""
    __titulo=""
    def __init__(self,codigo, nombre,titulo,duracion,tipo):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__titulo=titulo
        self.__duracion=duracion
        self.__tipo=tipo
    def nombre(self):
        return self.__nombre
    def codi(self):
        return self.__codigo
    def __str__(self):
        return f""" Codigo carrera: {self.__codigo})\n {self.__nombre}\n Titulo: {self.__titulo}\n Duracion: {self.__duracion}"""

 
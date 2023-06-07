from Clasecarrera import Carrera
class Facultad:
    __codigo=""
    __nombre=""
    __direccion=""
    __localidad=""
    __telefono=""
    def __init__(self,codigo,nombre,direccion,localidad,telefono):
        self.__codigo=int(codigo)
        self.__nombre=nombre
        self.__direccion=direccion
        self.__localidad=localidad
        self.__telefono=telefono
        self.__carrera=[]
    def cargarCarrera(self,codigo, nombre,fechadeinicio,duracion,titulo):
        self.__carrera.append(Carrera(codigo, nombre,fechadeinicio,duracion,titulo))
    def __str__(self):
        return (f"""{self.__codigo}{self.__nombre}\n direccion: {self.__direccion} localidad: {self.__localidad}""")
    def mostrarCarrera(self):
        for i in self.__carrera:
            print(i)
    def buscar2(self, nom):
        i=0
        band=False
        while band==False and i<len(self.__carrera):
            if self.__carrera[i].nombre()==nom:
                band=True
                print(f"{self.__codigo}.{self.__carrera[i].codi()} {self.__nombre} {self.__localidad}")
            else:
                i+=1
                
                                
    # def getCod(self):
    #     return self.__codigo
    # def getNom(self):
    #     return self.__nombre
    # def getDir(self):
    #     return self.__direccion
    # def getLoc(self):
    #     return self.__localidad
    # def getTel(self):
    #     return self.__telefono
        
                
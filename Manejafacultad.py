from Clasefacultad import Facultad
from Clasecarrera import Carrera
import csv
class manejaFacultad:
    def __init__(self):
        self.__lista=[]
    def agrega(self,codigo,nombre,direccion,localidad,telefono):
        self.__lista.append(Facultad(codigo,nombre,direccion,localidad,telefono))
    def cargar(self,archi='Facu.csv'):
        archivo=open(archi)
        reader=csv.reader(archivo,delimiter=',')
        i=0
        for fila in reader:
            if int(fila[0])!=i:
                self.__lista.append(Facultad(fila[0],fila[1],fila[2],fila[3],fila[4]))
                i+=1
            else:
               self.__lista[i-1].cargarCarrera(fila[1],fila[2],fila[3],fila[4],fila[5]) 
    def mostrar(self,i):
        i-=1
        self.__lista[i].mostrarCarrera()
    def mostrar2(self, nom):
        for fac in self.__lista:
            fac.buscar2(nom)
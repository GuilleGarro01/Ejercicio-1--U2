from Clasecarrera import Carrera
from Clasefacultad import Facultad
from Manejafacultad import manejaFacultad
import csv
if __name__=='__main__':
    unaFacu=manejaFacultad()
    print ("-------MENU-------")
    print ("1. Mostrar nombre y duracion, de las carreras ")
    print ("2. Buscar carrera por su nombre ")
    print ("3. Salir")
    opc=int(input("Ingrese opcion "))
    unaFacu.cargar()
    while opc!=3:
        if opc==1:
            cod=int(input("Ingrese codigo de la Facultad "))
            unaFacu.mostrar(cod)
        if opc==2:
            nomc=input("Ingrese el nombre de la carrera ")
            unaFacu.mostrar2(nomc)
    print ("-------MENU-------")
    print ("1. Mostrar nombre y duracion, de las carreras ")
    print ("2. Buscar carrera por su nombre ")
    print ("3. Salir")
    opc=int(input("Ingrese opcion "))
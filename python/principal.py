#Importacion de la clase modelo
from paquete.modelo import *

d= Docente("Docente de Economia","Cuenca")
d2= Docente("Docente de Biologia","Manabi")

listado=[d,d2]

e=Estudiante("Juan",listado)

print(e.presentar_datos())
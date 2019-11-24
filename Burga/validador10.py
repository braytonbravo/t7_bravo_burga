import os
#DECLARAR VARIABLES
fuerza,area,presion=0,0,0

#input
fuerza=int(os.sys.argv[1])
area=int(os.sys.argv[2])

#processing
presion=round(fuerza/area)

#VALIDAR LA LA PRESION QUE EJERCE UN CUERPO
presion_invalido=True
while(presion_invalido):
    presion=int(input("ingresar la distancia del auto"))
    presion_invalido=(presion<30 or presion >80)
#fin_while
print("fin del bucle")


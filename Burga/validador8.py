import os
#DECLARAR VARIABLES
fuerza,distancia,trabajo=0,0,0

#input
fuerza=int(os.sys.argv[1])
distancia=int(os.sys.argv[2])

#processing
trabajo=round(fuerza*distancia)

#VALIDAR EL TRABAJO QUE REALIZA UNA MAQUINA
trabajo_invalida=True
while(trabajo_invalida):
    trabajo=int(input("ingresar el trabajo que realiza una maquina "))
    trabajo_invalido=(trabajo<42 or trabajo>60)
#fin_while
print("fin del bucle")

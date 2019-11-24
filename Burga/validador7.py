import os
#DECLARAR VARIABLES
distancia,velocidad,tiempo=0,0,0

#input
velocidad=int(os.sys.argv[1])
tiempo=int(os.sys.argv[2])

#processing
distancia=round(velocidad*tiempo)

#VALIDAR LA DISTANCIA DE UN AUTO
distancia_invalida=True
while(distancia_invalida):
    distancia=int(input("ingresar la distancia del auto"))
    distancia_invalida=(distancia<22 or distancia>80)
#fin_while
print("fin del bucle")

import os
#DECLARAR VARIABLES
potencia_util,potencia_perdida,potencia_entregada=0,0,0

#input
potencia_util=int(os.sys.argv[1])
potencia_perdida=int(os.sys.argv[2])

#processing
potencia_entregada=round(potencia_util+potencia_perdida)

#VALIDAR EL POTENCIAL ENTREGADA DE UNA MAQUINA
potencia_entregada_invalida=True
while(potencia_entregada_invalida):
    potencia_entregada=int(input("ingresar la potencia entregada de una maquina  "))
    potencia_entregada_invalida=(potencia_entregada<100 or potencia_entregada>200)
#fin_while
print("fin del bucle")

import os
#DECLARACION DE LAS VARIABLES
fuerza,distancia,tiempo=0,0,0

fuerza=int(os.sys.argv[1])
distancia=int(os.sys.argv[2])
tiempo=int(os.sys.argv[3])

#PROCESSING
potencia=(fuerza*distancia)/tiempo

#VALIDAR POTENCIA
potencia_invalida=True
while (potencia_invalida):
    potencia=int(input("Ingrese potencia:"))
    potencia_invalida=(potencia>100 or potencia<200)
#fin_if
print("fin del bucler")

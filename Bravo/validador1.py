import os
#DECLARACION DE LAS VARIABLES
base_mayor,base_menor,altura=0.0,0.0,0

base_menor=float(os.sys.argv[1])
base_mayor=float(os.sys.argv[2])
altura=int(os.sys.argv[3])

#PROCESSING
area=((base_mayor+base_menor)/2)*altura

#VALIDAR EL AREA DE TRAPECIO
area_invalida=True
while (area_invalida):
    area=float(input("Ingrese area:"))
    area_invalida=(area>24 or area<45.4)

#fin_while
print("fin del bucler")

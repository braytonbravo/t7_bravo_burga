import os
#DECLARAR VARIABLES
base,altura=0,0,0

#input
base=int(os.sys.argv[1])
altura=int(os.sys.argv[2])

#processing
area=round(base*altura)/2

#VALIDAR el area de un triangulo
area_invalida=True
while(area_invalida):
   area=int(input("ingresar el area del triangulo "))
   area_invalida=(area<0 or area>30)
#fin_while
print("fin del bucle")

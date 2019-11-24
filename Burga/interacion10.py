import os
#input
nro_carnet=int(os.sys.argv[1])
#validador de datos
nro_carnet_invalido=(nro_carnet !="6847796")

while(nro_carnet_invalido):
    nro_carnet=input("ingrese el numero de carnet  ")
    nro_carnet_invalido=(nro_carnet!="6847796")

#processing
for numero in nro_carnet:
    print(numero)
#fin_iterar
print("fin del bucle")

#ouput
print("numero de carnet :",nro_carnet)

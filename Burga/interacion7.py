import os
#input
nro_dni=os.sys.argv[1]
#validador de datos
nro_dni_invalido=(nro_dni !="72326111")

while(nro_dni_invalido):
    nro_dni=input("ingrese el numero de dni ")
    nro_dni_invalido=(nro_dni!="72326111")

#processing
for numero in nro_dni:
    print(numero)
#fin_iterar
print("fin del bucle")

#ouput
print("numero de dni :",nro_dni)

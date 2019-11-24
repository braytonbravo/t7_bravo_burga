import os
#input
contraseña=int(os.sys.argv[1])
#validador de datos
contraseña_invalido=(contraseña !="655845")

while(contraseña_invalido):
    contraseña=input("ingrese la contraseña  ")
    contraseña_invalido=(contraseña!="655845")

#processing
for numero in contraseña:
    print(numero)
#fin_iterar
print("fin del bucle")

#ouput
print("numero de contraseña :",contraseña)

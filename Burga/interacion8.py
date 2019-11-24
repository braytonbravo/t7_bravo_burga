import os
#input
codigo_de_barra=int(os.sys.argv[1])
#validador de datos
codigo_de_barra_invalido=(codigo_de_barra!="45222631989")

while(codigo_de_barra_invalido):
    codigo_de_barra=input("ingrese el numero del codigo de barra")
    codigo_de_barra_invalido=(codigo_de_barra!="45222631989")

#processing
for numero in codigo_de_barra:
    print(numero)
#fin_iterar
print("fin del bucle")

#ouput
print("abecedario:",codigo_de_barra)

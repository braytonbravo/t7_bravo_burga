import os
#DECLARACION DE LAS VARIABLES
nota1,nota2,nota3=0,0,0

nota1=int(os.sys.argv[1])
nota2=int(os.sys.argv[2])
nota3=int(os.sys.argv[3])

#PROCESSING
promedio=(nota1+nota2+nota3)/3

#VALIDAR EL PROMEDIO DE LAS NOTAS
promedio_invalida=True
while (promedio_invalida):
    promedio=int(input("ingrese promedio:"))
    promedio_invalida=(promedio>=0 or promedio<=20)
#fin_while
print("fin del bucler")

import os
#DECLARACION  DE LAS VARIABLES
cliente,arroz,manzana,aceite="",0.0,0.0,0.0

cliente=os.sys.argv[1]
arroz=float(os.sys.argv[2])
manzana=float(os.sys.argv[3])
aceite=float(os.sys.argv[4])

#PROCESSING
total=(arroz+manzana+aceite)

#VALIDAR EL TOTAL A PAGAR
total_invalida=True
while (total_invalida):
    total=float(input("Ingrese total:"))
    total_invalida=(total>11.3 or total<15.6)
#fin_while
print("fin del bucler")

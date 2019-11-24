import os
#DECLARACION DE LAS VARIABLES
cliente,precio_de_licuadora,precio_de_lavadora,precio_del_televisor="",0.0,0.0,0.0

cliente=os.sys.argv[1]
precio_de_licuadora=float(os.sys.argv[2])
precio_de_lavadora=float(os.sys.argv[3])
precio_del_televisor=float(os.sys.argv[4])

# PROCESSING
precio_total=round(precio_de_licuadora+precio_de_lavadora+precio_del_televisor)

#VALIDAR EL PRECIO TOTAL DE LOS PRODUCTOS
precio_total_invalida=True
while (precio_total_invalida):
    precio_total=float(input("Ingrese el precio total:"))
    precio_total_invalida=(precio_total>11.20 or precio_total<91.3)
#fin_while
print("fin del bucler")

# Decodificar mensaje encriptado
# A = Hola
# B = te extraño
# F = Te veo
# R = Cuidate
msg="AABFR"

for letra in msg:
    if letra == "A":
        print("Hola")
    if letra == "B":
        print("te extraño")
    if letra == "F":
        print("Te veo")
    if letra == "R":
        print("Cuidte")
#fin_iterador

print("Fin del bucle")

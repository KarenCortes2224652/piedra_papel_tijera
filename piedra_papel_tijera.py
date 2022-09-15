# Jugar Piedra, Papel y Tijera con el pc.

import random
print("-------------------------------")
print("--- PIEDRA - PAPEL - TIJERA ---")
print("-------------------------------")

#Input
while True:
 aleatorio = random.randrange(0, 3)
 elijePc = ""
 print("1. Piedra")
 print("2. Papel")
 print("3. Tijera")
 opcion = int(input("Elige una opción: "))

 if opcion == 1:
    elijeUsuario = "Piedra"
 elif opcion == 2:
    elijeUsuario = "Papel"
 elif opcion == 3:
    elijeUsuario = "Tijera"
 print("Tu elijes: ", elijeUsuario)

 if aleatorio == 0:
    elijePc = "Piedra"
 elif aleatorio == 1:
    elijePc = "Papel"
 elif aleatorio == 2:
    elijePc = "Tijera"
 print("PC elijio: ", elijePc)
 print("...")
 if elijePc == "Piedra" and elijeUsuario == "Papel":
    print("Ganaste")
 elif elijePc == "Papel" and elijeUsuario == "Tijera":
    print("Ganaste")
 elif elijePc == "Tijera" and elijeUsuario == "Piedra":
    print("Ganaste")
 if elijePc == "Papel" and elijeUsuario == "Piedra":
    print("Perdiste")
 elif elijePc == "Tijera" and elijeUsuario == "Papel":
    print("Perdiste")
 elif elijePc == "Piedra" and elijeUsuario == "Tijera":
    print("Perdiste")
 elif elijePc == elijeUsuario:
    print("Empate")

#Fin
import random

print("Bienvenidos al Juego de los dados")
print("Vamos a comenzar")
name = input("Cual es tu nombre?: ")

print(f"Escribe ya cuando estes listo para comenzar {name}")
activar = input("Ya?").lower()
dado1 =random.randint(1, 6)
dado2 =random.randint(1, 6)

if activar == "ya":
    if dado1 > dado2:
        print(f"El tu dado fue : {dado1} y el de la computadora fue: {dado2}")
        print("Ganaste!")
    elif dado1 == dado2:
        print(f"El tu dado fue : {dado1} y el de la computadora fue: {dado2}")
        print("Empataste!")
    else:
        print(f"El tu dado fue : {dado1} y el de la computadora fue: {dado2}")
        print("Perdiste!")
else:
    print("Perdon, esa accion no la reconozco")
 


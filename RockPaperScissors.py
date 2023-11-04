import random

# Definimos las opciones de juego
opciones = ["piedra", "papel", "tijera"]

# Pedimos la jugada del usuario
jugada_usuario = input("Elige piedra, papel o tijera: ").lower()

# Generamos la jugada de la computadora
jugada_computadora = random.choice(opciones)

print("Tu jugada: " + jugada_usuario)
print("La jugada de la computadora: " + jugada_computadora)

if jugada_usuario == jugada_computadora:
    print("Empate!")
elif (jugada_usuario == "papel") and (jugada_computadora == "piedra"):
    print("Ganaste!")
elif (jugada_usuario == "papel") and (jugada_computadora == "tijera"):
    print("Perdiste!")
elif (jugada_usuario == "tijera") and (jugada_computadora == "papel"):
    print("Ganaste!")
elif (jugada_usuario == "tijera") and (jugada_computadora == "piedra"):
    print("Perdiste!")
elif (jugada_usuario == "piedra") and (jugada_computadora == "papel"):
    print("Perdiste!")
else:
    print("Ganaste!")

print("Gracias por Jugar!")

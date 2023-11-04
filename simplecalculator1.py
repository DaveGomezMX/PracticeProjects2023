numero1 = int(input("Ingrese el primer digito: "))
numero2 = int(input("Ingrese el segundo digito: "))
accion = input("Seleccione entre sumar, restar, multiplicar: ")

if accion == "sumar":
    resultado = numero1 + numero2
elif accion == "restar":
    resultado = numero1 - numero2
else:
    resultado = numero1 * numero2

print("El resultado es:", resultado)
print("Gracias por usar la calculadora.")

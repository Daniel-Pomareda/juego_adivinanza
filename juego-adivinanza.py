import random

numero_secreto = random.randint(1,100)
cant_intentos = 0
cant_maxima = 5
adivinando = False

print("¡Bienvenido al juevo de adivinar el numero secreto!")

while not adivinando:
    if not cant_intentos < cant_maxima:
        print("¡Game Over!")
        break

    entrada = input("introduce un numero del 1 al 100: ")
    numero = int(entrada)

    if numero == numero_secreto:
        print("Felicidades, lograste encontrar el numero secreto")
        adivinando = True
    elif numero < numero_secreto:
        print("El numero secreto es mayor al ingresado")
    else:
        print ("El numero secreto es menor al numero ingresado")

    cant_intentos += 1
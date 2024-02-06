import random

secreto = random.randint(1,10)

numero = int(input("Adivina el numero entre 1 y 10"))

while numero != secreto:
    if numero < secreto:
        print("El numero es mayor")
    else:
        print("El numero es menor")

    
    numero = int(input("Intenta denuevo: "))

print ("Felicitaciones! adivinasteee el numero secreto: ", secreto)
print("fin")

    
def ingresar():
    enteros= []

    for n in range(5):
        numero=int(input("Ingrese el numero: "))
        enteros.append(numero)
    
    imprimir(enteros)
    sumar(enteros)


def imprimir(enteros):

    print("Los datos ingresados son: ")
    for n in enteros:
        print(n)

def sumar(enteros):
    num=0
    for n in enteros:
        num=num+n

    print(f"La suma es:", num)



ingresar()

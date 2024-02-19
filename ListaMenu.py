lista=[]

def agregar():
    num=int(input("Ingrese el numero a añadir a la lista:"))
    lista.append(num)
    print(f"EL numero {num} fue añadido a la lista.")


def agregar_posicion():
    num=int(input("Ingrese el numero a añadir: "))
    pos=int(input("Ingrese la posicion donde añadir el numero: "))
    lista.insert (pos -1, num)
    print(f"EL numero {num} fue añadido a la lista en la posicion {pos}.")


def longitud ():
    print ("La longitud de la lista es de: ", len(lista) )



def eliminar_ultimo():
    ultimo= lista.pop(-1)
    print("Se ha eliminado de la lista el numero: ", ultimo )


def eliminar():
    pos=int(input("Ingrese la posicion del elemento: "))

    if 1<=pos<=len(lista):
        eliminado=lista.pop(pos-1)
        print(f"El numero eliminado es: {eliminado}")
    else: 
        print("La posicion ingresada no es valida")


def contar_num():
    num=int(input("Ingrese el numero a contar: "))
    contador=lista.count(num)
    print(f"El numero {num} está {contador} veces en la lista.")


def posicion_numero():
    num=int(input("Ingrese el numero para conocer su posicion: "))

    for i in range (len(lista)):
        if lista[i]==num:
            print("El numero esta en la posicion", i+1)
    

def mostrar():
    print("Los  numeros de la lista son: ", lista)



while True:
    print("MENÚ DE LISTA")
    print("1. Añadir número")
    print("2. Añadir número con posición")
    print("3. Longitud de lista")
    print("4. Eliminar último número")
    print("5. Eliminar número")
    print("6. Contar lista")
    print("7. Posicion de un número")
    print("8. Mostrar listaa")
    print("9. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        agregar()
    elif opcion == 2:
        agregar_posicion()
    elif opcion == 3:
        longitud()
    elif opcion == 4:
        eliminar_ultimo()
    elif opcion == 5:
        eliminar()
    elif opcion == 6:
        contar_num()
    elif opcion == 7:
        posicion_numero()
    elif opcion == 8:
        mostrar()
    elif opcion == 9:
        print("Fin el programa")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

    



    







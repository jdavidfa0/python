
ancho= int(input("Ingrese el ancho"))
altura =int(input("Ingrese la altura"))
caracter=input("Ingresar el caracter")

def dibujar(anch, altu, cara):
    for i in range(anch):
        for j in range(altu):
            print(cara, end="")
        print()


#dibujar (ancho, altura, caracter)





def principal():
    cesta={

    }
    mostrar(cesta)
    conti='s'

    while conti=='s' or conti =='S':
        print("INGRESE ARTICULOS") 
        nomarti=input("Ingrese nombre del articulo: ")
        articulos=[]
        while True:
            prearti=float(input("Ingrese el precio del articulo: "))
            articulos.append((prearti))
            break
        conti=input("¿Desea ingresar otro articulo? s/n: ")
        cesta[nomarti]=articulos
    return cesta


def mostrar (cesta):
    print("LISTADO GUARDADO")
    for nomarti in (cesta):
        print("Articulo", nomarti,'', end='')
        for prearti in cesta[nomarti]:
            print("Precio:  ", prearti )
          



cesta=principal()
mostrar(cesta)

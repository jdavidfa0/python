
def principal():
    dic_frutas={

    }
    mostrar(dic_frutas)

    conti='s'

    while conti=='s' or conti =='S':
        print("INGRESE UNA FRUTA ") 
        nomfru=input("Ingrese nombre de la fruta: ")
        frutas=[]
        while True:
            prefru=float(input("Ingrese el precio de la fruta: "))
            cantfru=int(input("Ingrese cantidad que se ha vendido: "))
            total=cantfru*prefru
            frutas.append((prefru,cantfru,total))
            break
        conti=input("¿Desea ingresar otra fruta? s/n: ")
        dic_frutas[nomfru]=frutas
    return dic_frutas




def mostrar (dic_frutas):
    print("LISTADO GUARDADO")
    for nomfru in (dic_frutas):
        print("Fruta:", nomfru)
        for prefru,cantfru,total in dic_frutas[nomfru]:
            print("-Precio:  ", prefru )
            print("-Cantidad: ",cantfru)
            print("-Valor total: ", total)


def consultar (dic_frutas):
   
    nomfru=input("Ingrese la fruta que quiere consultar: ")
    while True:
        if nomfru in dic_frutas:
            for prefru,cantfru,total  in dic_frutas[nomfru]:
                print("-Precio:  ", prefru )
                print("-Cantidad: ",cantfru)
                print("-Valor total: ", total)  

        else:
            print("No existe registro de esa fruta")
        conti=input("¿Desea consultar una fruta? s/n: ") 
        if conti.lower() !='s':
            break
        nomfru=input("Ingrese la fruta que quiere consultar: ")
    

dic_frutas=principal()
mostrar(dic_frutas)
consultar(dic_frutas)



    
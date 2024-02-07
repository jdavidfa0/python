


def inicio():
    print("MENU PRINCIPAL")
    print ("Selecciones una opcion: ")
    print ("1.Sumar")
    print("2.Restar")
    print("3.Multiplicar")
    print("4.Dividir")
    print("5.Salir")


def main():
    while True: 
        inicio()
        opcion=int(input("Selecione una opcion"))
        if opcion ==1:
            print("Ha seleccionado Sumar: ")
            num1=int(input("Ingrese el 1 numero:"))
            num2=int(input("Ingrese el 2 numero: "))
            sumar=num1+num2
            print ("El resultado de la suma es: ", sumar)

        elif opcion==2:
            print("Ha seleccionado Restar: ")
            num1=int(input("Ingrese el 1 numero:"))
            num2=int(input("Ingrese el 2 numero: "))
            resta=num1-num2
            print ("El resultado de la suma es: ", resta)
        
        elif opcion ==3:
            print("Ha seleccionado Multiplicar: ")
            num1=int(input("Ingrese el 1 numero:"))
            num2=int(input("Ingrese el 2 numero: "))
            multi=num1*num2
            print ("El resultado de la Multiplicacion es: ", multi)
        elif opcion==4:
            print("Ha seleccionado Dividir: ")
            num1=float(input("Ingrese el 1 numero:"))
            num2=float(input("Ingrese el 2 numero: "))
            dividir=num1/num2
            print ("El resultado de la division es: ", dividir)
        elif opcion ==5:
            print("Hasta luegooo")
            break
        
        else:
            print("Ingrese una opcion valida...")


inicio()
main()
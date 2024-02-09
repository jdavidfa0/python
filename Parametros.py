
texto= "Buenos dias, definiendo un parametro en una funcion"
#Funcion sin parametros
def mensaje():
    n1= int(input("Ingrese el primer numero"))
    n2= int(input("Ingrese el segundo numero"))
    calculador_mayor(n1,n2)
    positivo (n1,n2)
#funcion con parametros
def calculador_mayor(num1,num2):
    if num1>num2:
        print("El primer numero es mayor")

    elif num1==num2:
        print ("Son numeros iguales")
    
    else:
        print("El segundo numero es mayor")



def positivo(p1,p2):
    if p1>=0 and p2>=0:
        print("Numeros positivos")
    elif p1<0 and p2>=0:
        print(f"{p1} es negativo y {p2} es positivo")
    else:
        print("Numeros negativo")


mensaje()

def añonor():
    a =int(input("Ingrese el año: "))
    bisiesto(a)

def bisiesto(a):

    if (a%4==0) and (a%100 !=0):
        print(f"{a} Es bisiesto")
    else:
        print(f"{a} No es bisiesto")

añonor()
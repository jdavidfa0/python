cont =0
acum =0
alturas =int(input("Ingrese cantidad de alturas"))

while cont<alturas:
    num= int(input("Ingrese altura:  "))
    acum=acum+num

    cont+= 1
Promedio = acum/alturas

print ("La suma de alturas es: ", acum)
print ("El promedio de alturas es: ",Promedio)

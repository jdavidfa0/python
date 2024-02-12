
conduc=[]
kilom=[]
total_kim=[]
sumtotal=0
cant=int(input("Ingrese cantidad de conductores: "))
for i in range (cant):
    conductor=input("Ingrese nombre del conductor: ")
    conduc.append(conductor)
    kilom=[]

    for n in range (1,8):
       kim=float(input(f"Ingrese kilometros del dia {n}: "))
   
       kilom.append(kim)

       sumtotal=0
    for x in range(len(kilom)):
        sumtotal+= kilom[x]
    total_kim.append(sumtotal)


print(total_kim)

for n in range(cant): 
    print(f"Conductor: {conduc[n]}  Kilometros: {total_kim[n]}")
  

conti=0
contf=0

inicio= int (input("Ingrese primer año: "))
fin =int (input("Ingrese el ultimo año"))

for i in range(inicio,fin+1):
    
    if (i%4==0) and (i%100 !=0):
       conti+=1
    else:
         contf+=1

print(f"Hay {conti} años bisiestos")
print(f"Hay {contf} años no bisiestos")




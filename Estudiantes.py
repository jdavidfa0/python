mañanasum=0
tardesum=0
nochesum=0

for cont in range (6):
    mañana=int(input("Ingrese edades de los Estudiantes de Mañana "))
    mañanasum=mañanasum+mañana


for cont in range (7):
    tarde=int(input("Ingrese edades de los Estudiantes de Tarde"))
    tardesum=tardesum+tarde


for cont in range (12):
    noche=int(input("Ingrese edades Estudiantes de Noche"))
    nochesum=nochesum+noche

prom=(mañanasum)/6
prom1=(tardesum)/7
prom2=(nochesum)/12

print("Promedio Estudiantes de la mañana", prom)
print("Promedio Estudiantes de la tarde", prom1)
print("Promedio Estudiantes de la noche", prom2)
if prom >prom1 and prom>prom2:
    print("Los estudiantes de la mañana tienen mayor promedio de edad : ", prom)
elif prom1>prom and prom1>prom2:
    print("Los estudiantes de la tarde tienen mayor promedio de edad  : ", prom1)
else:
    print("Los estudiantes de la noche tienen mayor promedio de edad : ", prom2)

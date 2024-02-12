alumno=[]
notas=[]
mejores=[]
buenos=[]
eliminar=[]
cont=0
contb=0
conti=0
for i in range(1,5):
    nombre=input(f"Ingrese el nombre del alumno {i}: ")
    alumno.append(nombre)
    nota=int(input("Ingrese la nota del alumno: "))
    notas.append(nota)


for i in range (len(alumno)):
    print(alumno[i])
    print(notas[i])

    if notas[i] >=8:
        print("Muy bueno")
        cont+=1
        mejores.append(alumno[i])
    elif notas[i] >=4:
        print("Bueno")
        buenos.append(alumno[i])
        contb+=1
    else:
        print("Insuficiente")
        conti+=1


for n in range (len(notas)):
    if 4 <=notas[n]<=7:
        eliminar.append(n)

for d in sorted (eliminar, reverse=True):
        notas.pop(d)
        alumno.pop(d)



print("Listado de alumnos con notas entre 4 y 7 :", alumno)

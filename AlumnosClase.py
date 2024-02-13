
alumnos={}

cant = int(input("Ingrese cantidad de alumnos: "))

for x in range(cant):
    nombre = input("Ingrese el nombre del alumno:  ")
    nota=0
   
    Notas = []
    while nota >= 0:
     nota = float(input("Ingrese la nota del alumno: "))
     Notas.append(nota)

     alumnos[nombre]=Notas

for nombre in alumnos:
   print(nombre)
   sum=0
   for nota in alumnos[nombre]:
      
      sum+=nota

      print(nombre,sum)


   
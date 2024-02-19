
def principal():
    alumnos={

    }
    mostrar(alumnos)

    cant = int(input("Ingrese cantidad de alumnos: "))

    for x in range(cant):
        nombre = input("Ingrese el nombre del alumno:  ")
        if nombre in alumnos:
            print("**Error*Nombre ya registrado")
            break
        
        Notas = []
        while True:
            nota = float(input("Ingrese la nota del alumno: ")) 
            Notas.append(nota)
            if nota<0:
                break
        alumnos[nombre]=Notas
    return alumnos


def mostrar (alumnos):
    print("LISTADO DE ALUMNOS")
    for nombre in (alumnos):
        print("Nombre: ", nombre)
        for nota in alumnos[nombre]:
            print(nota)


def promediar(alumnos):
    for nombre, Notas in alumnos.items():
        promedio=sum(Notas)/len(Notas)
        print("El promedio de los alumnos es:")
        print("Nombre ", nombre,'', end='')
        print("Nota: ", promedio)











alumnos=principal()
mostrar(alumnos)
promediar(alumnos)
    
    



   
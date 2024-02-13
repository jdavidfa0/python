def registrar():
    
    agenda={
    }
    Respuesta="s"

    while Respuesta=="s":
        fecha=input("Ingrese la Fehca DD/MM/AAAA: ")
        lista=[]
        while Respuesta=="s":
            hora=input("Ingrese la hora de la actividad h/m: ")
            actividad=input("Ingrese nombre de la actividad")
            lista.append((hora,actividad))
            Respuesta=input("Desea ingresar un actividad para la misma Fecha: s/n ")
        agenda[fecha]=lista
        Respuesta=input("Desea ingresar otra fecha: s/n")
    return agenda

def mostrar (agenda):
    print("Listado de la agenda")
    for fecha in agenda:
        print("Para la fecha: ", fecha)
        for hora,actividad in agenda[fecha]:
            print(hora, actividad)

def consultarfecha (fecha):
    fecha=input("Ingrese la fecha que quiere consultar: ")
    if fecha in agenda:
        for hora,actividad in agenda[fecha]:
            print(hora,actividad)
    else:
        print("No existen actividades para la fecha")

agenda=registrar()
mostrar(agenda)
consultarfecha(agenda)


import random

print("MENU PRINCIPAL")
print("1.Juego de dados")
print("2.Grupos A y B")
print("3.Precio salas de juegos")
print("4.Contraseña")
print("5.Cáculo Factura ")
print("6.Salir")

def salas():
    print ("Precio salas de juego")
    edad=int(input("Ingrese edad:  "))
    if edad<4:
        print("Ingresa gratis...")
    elif edad>=4 and edad<18:
        print("Cancela $30.000")
    else:
        print("Cancela $50.000")

def fac():
    print("Cálculo Factura:")
    factura=float(input("Digite la cantidad sin IVA: "))
    iva= float(input("Ingrese el valor IVA a aplicar: "))
    
    if iva!=0:
        facturai=(factura*iva)/100
        factura_to=(factura+facturai)
        print(f"El total es: {factura_to}")
    elif iva==0:
        facturai=(factura*21)/100
        factura_to=(factura+facturai)
        print(f"El total es: {factura_to}")

def grupos():
    genero=input("Ingrese su genero f/m:  ")
    nombre=input("Ingrese su nombre: ")

    if  (genero.lower()=="f") and ( nombre.lower()<"m"):
        print(f"{nombre}Pertenece al grupo A")
    elif (genero.lower()=="m") and ( nombre.lower()>"n"):
        print(f"{nombre} Pertenece al grupo A")
    elif (genero.lower()=="f") and ( nombre.lower()>"m"):
        print(f"{nombre} Pertenece al grupo B")
    elif (genero.lower()=="m") and ( nombre.lower()<"n"):
        print(f"{nombre} Pertenece al grupo B")


def dados():
    alvaro=random.randint(1,6)
    barbara=random.randint(1,6)

    if (alvaro==barbara):
        print(f"Álavaro sacó: {alvaro}")
        print(f"Bárbara sacó: {barbara}")
        print("Han empatado")
    elif (alvaro<barbara):
        print(f"Álavaro sacó: {alvaro}")
        print(f"Bárbara sacó: {barbara}")
        print("Bárbara ha ganado")
    elif (alvaro>barbara):
        print(f"Álavaro sacó: {alvaro}")
        print(f"Bárbara sacó: {barbara}")
        print("Álvaro ha ganado")

def contra():
    clave=input("Digite su contraseña: ")
    clave2=input("Confirme su contraeña: ")
    if (clave==clave2):
        print("Clave correcta")
    while (clave!=clave2):
        print("Intente denuevo..")
        clave2=input("Digite su contraseña: ")
  

while True: 
    opc= int(input("ELIGE UNA OPCIÓN: "))

    if opc==1:
        dados()

    elif opc==2:
        grupos()
    
    elif opc==3:
        salas()
    
    elif opc==4:
        contra()

    elif opc==5:
        fac()
    else:
        print("Fin del promgrama...")
        break

tupla= (2,3,4)
fecha=(9,"febrero", 2024)

palabras=int(input("Ingrese cantidad de palabras a agregar"))

if palabras<1:
    print("No valido")
else:
    lista=[]
    for n in range(palabras):
        palabra=input(f"Ingrese la palabra {n+1}")
        lista +=[palabra]
    print(f"La lista creada es: {lista}")
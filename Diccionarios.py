Persona={
    "Nombre":"David",
    "Apellido":"Fandino",
    "Estatura":1.80,
    "Edad":19,
    "Email": "jdavidfa0@gmail.com",
    "CiudadNac": "Bogotá",
    "Genero":["Femenino", "Masculino", "Otro"]

}
#Mostrar diccionarios
print(Persona["Edad"], Persona["CiudadNac"])
#Agregar a dicionario
Persona["Telefono"]=3227055094
print(Persona["Telefono"])
#Modificar elementos
Persona["Celular"]=Persona.pop("Telefono")
#Eliminar del diccionario
del Persona["Celular"]
print(Persona)

#iterar los item de las claves y valores

for clave,valor in Persona.items():
    print( clave, ":", valor)
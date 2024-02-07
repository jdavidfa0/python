n = int(input("Ingrese Numero Empleados"))
cont1=0
cont2=0
gasto=0

for cont in range(n):
    sueldo =float(input("Ingrese el valor sueldo del empleado"))
    gasto =gasto+sueldo

    if sueldo>=1300000 and sueldo<=3000000:
        cont1+=1
    elif sueldo> 3000000:
        cont2+=1

print("Los gastos totales de la empresa son: ", gasto)
print("Empleados ganan entre 1.300.000 y 3.000.000:  ", cont1 )
print("Empleados ganan mas de 3.000.000:  ", cont2 )
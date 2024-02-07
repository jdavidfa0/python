

cont=0
contt=0
sueldos1 =0
sueldos2=0
sueldoscant = int(input("Digite cantidad de sueldos:"))
sueldoscont=0
while sueldoscont<sueldoscant:
    
    sueldo= float(input("Ingrese el sueldo"))

    if sueldo>= 3000000 and sueldo<=10000000:

        sueldos1=sueldos1+sueldo
        cont+=1
    elif sueldo>=1300000 and sueldo<3000000:

        sueldos2=sueldos2+sueldo
        contt+=1
    sueldoscont+=1
print("Empleados entre 3.000.000 y 10.000.000", cont)
print("Pago total de empleados:",sueldos1)
print("Empleados entre 1.300.000 y 3.000.000", contt)
print("Pago total de empleados:",sueldos2)


    


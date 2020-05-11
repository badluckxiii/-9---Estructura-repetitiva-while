# En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, 
# realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos 
# empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa
# deberá informar el importe que gasta la empresa en sueldos al personal. 
vector=[]
iterador=0
print('Cuantos trabajadores tiene tu empresa:')
numero=int(input())
while iterador <numero:
    sueldo=int(input('Sueldo:'))
    vector.append(sueldo)
    iterador+=1
n=0
minimo=0
maximo=0
suma=0
while n<len(vector):
    suma+=vector[n]
    if vector[n]>=100 and vector[n]<300:
       minimo+=1
    elif vector[n]>=300:
        maximo+=1
    n+=1
print('Personas que cobran entre 100 y 300 $ ',minimo,
'\nPersonas que cobran mas de 299 ',maximo)
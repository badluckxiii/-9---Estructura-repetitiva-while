#  Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe 
# cuántos tienen notas mayores o iguales a 7 y cuántos menores. 
i=0
n=[]

while i<10:
    j=int(input('Valor de: '))
    n.append(j)
    i+=1
menors=0
majors=0
iterador=0
while iterador<len(n):
    if n[iterador]>=7:
        majors+=1
    else:
        menors+=1
    iterador+=1
print('menors de 7',menors,'\nmajors de 7',majors)

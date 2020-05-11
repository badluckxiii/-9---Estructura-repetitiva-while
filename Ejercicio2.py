alturas=[]
n=int(input('Numero de persones: '))
valor=0

while valor<n:
    print('Altura de persona: ')
    h=int(input('Altura:'))
    alturas.append(h)
    valor+=1
it=0
suma=0
while it<len(alturas)-1:
    suma+=alturas[it]
    print(suma)
    it+=1
promedio=suma/len(alturas)
print('promedio=',promedio)
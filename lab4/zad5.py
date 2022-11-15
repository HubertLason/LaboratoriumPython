import random

punkty = []

for i in range(15):
    x=round(random.uniform(1,50),2)
    punkty.append(x)

print(max(punkty))
print(min(punkty))

a=float(input("Podaj liczbę punktów: "))

if punkty.count(a)>0:
    print(punkty.index(a))
else:
    print("Taka liczba punktów nie występuje na liście")

suma=0

for i in range(15):
    suma+=punkty[i]
print(f"Średnia: {suma/15}")

powyzej=0
ponizej=0
powy=[]
poni=[]

for i in range(15):
    if punkty[i]>(suma/15):
        powyzej+=1
        powy.append(punkty[i])
    elif punkty[i]<(suma/15):
        ponizej+=1
        poni.append(punkty[i])

print(f"Ilość osób powyżej średniej: {powyzej}")
print(f"Ilość osób poniżej średniej: {ponizej}")
print(f"Punkty powyżej średniej: {powy}")
print(f"Punkty poniżej średniej: {poni}")



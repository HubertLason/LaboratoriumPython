import random

a=int(input("Podaj ilość elementów listy: "))
zestaw_1=[]
i=0

while i<a:
    zestaw_1.append(random.randint(1,10))
    i=i+1

print(zestaw_1)

zestaw_2=[]
j=0

while j<a:
    zestaw_2.append(random.randint(5,15))
    j=j+1

print(zestaw_2)

c=int(input("Podaj liczbę: "))

if zestaw_1.count(c)>0:
    print("Liczba z zestawu 1")
elif zestaw_2.count(c)>0:
    print("Liczba z zestawu 2")
else:
    print("Nie ma takiej liczby w obu zestawach")

zestaw_1_2=zestaw_1+zestaw_2
zestaw_1_2.sort()
print(zestaw_1_2)
suma=0
n=0

while True:
    b=int(input("Podaj liczbę punktów: "))

    if (b<0 or b>100):
        break
    else:
        suma=suma+b
        n=n+1


print (suma/n)

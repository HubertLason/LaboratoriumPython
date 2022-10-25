a = int(input("podaj liczbę a: "))
b = int(input("podaj liczbę b: "))

if b<a:
    a,b=b,a

while b>=a:
    if a%2==0:
        print(a,end=' ')
        a=a+1
    else:
        a=a+1
        continue

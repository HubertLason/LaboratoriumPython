print ('''Jaką operację chcesz wykonać?
1) dodawanie
2) odejmowanie
3) mnożenie
4) dzielenie
5) potęgowanie
''')

operacja = int (input("Wpisz numer operacji: "))
a = int (input("Podaj argument 1:"))
b = int (input("Podaj argument 2:"))

if operacja==1:
    print (f"Wynik:{a+b}")
elif operacja==2:
    print(f"Wynik:{a-b}")
elif operacja==3:
    print (f"Wynik:{a*b}")
elif operacja==4:
    if b==0:
        print ("Dzielenie przez 0")
        exit()
    print(f"Wynik:{a/b}")
elif operacja==5:
    print(f"Wynik:{a**b}")
else:
    print ("Niepoprawny numer opercacji")
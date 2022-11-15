imiona=['Kasia', 'Tomek', 'Jan', 'Ola', 'Jerzy', 'Marek', 'Piotr', 'Zuzia', 'Bartek', 'Jacek']
imiona[4]="Józef"
imiona.insert(5,"Janusz")
del imiona[7]
print(imiona)
imiona.insert(0, "Hubert")
imiona.insert(1, "Jakub")
imiona.insert(2, "Mariusz")

a=input("Podaj imie do usunięcia: ")
imiona.remove(a)
imiona[-1]="Krzysztof"
print(imiona[0:3],imiona[-3:])

b=input("Podaj imię:")
if imiona.count(b)>0:
    print("Imię znajduje sie na liście")
else:
    print("Imię nie znajduje sie na liście")
imiona.sort()
print(imiona)
imiona.reverse()
print(imiona)

l= len(imiona)//2

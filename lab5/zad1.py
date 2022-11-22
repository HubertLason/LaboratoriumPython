values=[10,20,30]
keys=['ten','twenty','thirty']
D={}
#print(list(zip(keys,values)))
#D=dict(zip(keys,values))
for i in range (len(values)):
    D[keys[i]]=values[i]
print(D)
D2=dict(thirty=30,fourty='40',fifty=50)
#D.update(D2)
D3=D.copy()
D3.update(D2)
print(D3)

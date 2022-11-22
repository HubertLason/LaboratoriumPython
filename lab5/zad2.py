sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}

for key in sample_dict:
 print(f"{key:<10}={sample_dict[key]:>10}")

L=['age','name']
'''D={}
for k in L:
 if k in sample_dict.keys():
  D[k]=sample_dict[k]
print(D)'''

for k in L:
 del sample_dict[k]
print(sample_dict)

if 'Jones' in sample_dict.values():
 print("Warość Jones występuje w słowniku")

sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)
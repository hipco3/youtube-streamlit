person={
    'name':'Bob',
    'age':25,
    'gender':'male'
}
print(person['gender'])

key='name'
print(person[key])
person['age']+=1
person['favorite']='りんご'
print(person)

print(person== {'name':'kitty', 'age': 26,'gender':'male'})
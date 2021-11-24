def mod_five(n):
    return n%5

numbers=[7,3,5,1,3]

print(sorted(numbers))
print(sorted(numbers,reverse=True))
print(sorted(numbers,key=mod_five)


meats=['bacon','niku','saw']

print(sorted(meats))
print(sorted(meats,reverse=True))
print(sorted(meats,key=len))
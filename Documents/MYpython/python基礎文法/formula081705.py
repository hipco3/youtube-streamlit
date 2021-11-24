members=['bob','tom','ivy']
my_iter=iter(members)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
members=['bob','tom','ivy']
print(list(enumerate(members)))

for i, member in enumerate(members):
    print(i,member)

letter='abc'
members=['bob','tom','ivy']
favorites=['apple','banana','grape']
print(list(zip(letter,members,favorites)))

for letter, member,favorite in zip(letter,members,favorites):
    print(letter,f'{member}は{favorite}がすきです')
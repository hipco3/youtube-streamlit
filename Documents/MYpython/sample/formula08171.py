print(abs(-123.45))
print(ord('A'))
print(chr(65))
print(chr(10))
print('bob','kitty','apple')
print('bob','kitty','apple',sep='/')

for member in ['bob','kitty','apple']:
    print(member, end='\t')
members= ['bob','kitty','apple']
member=input('member名をいれてください')   

if member in members:
    print(f'{member}はメンバーです') 
else:
    print(f'{member}はメンバーではありません')    
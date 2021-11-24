my_list=[]
for i in range(1,21):
    if i%3==0 or '3' in str(i):
        my_list +=[i]
print(my_list)


my_list=[i for i in range(1,21) if i%3 ==0 or '3' in str(i)]
print(my_list)
x=10
y=10
try:
    z=x/y
except ZeroDivisionError as e:
    print('ZeroDivisionErrorが発生')    
except TypeError as e:
    print('TypeError発生') 
else:
    print('例外の発生はなし') 
finally:
    print('例外処理終了します')          

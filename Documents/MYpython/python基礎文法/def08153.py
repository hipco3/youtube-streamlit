def func(*args,x):

    result = ', '.join(args)
    print(f'{x}:{result}')
    
func('a','kitty','good', x=33) 

def print_keyword_args(**kwargs):
    print(kwargs)

print_keyword_args(name='miffy',age=25)  


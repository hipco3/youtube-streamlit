def print_area(x,y):
    print(f'縦{x},横{y}の長方形の面積は{x*y}です')
print_area(3,2)    
print_area(1000,35)

def tri_area(base,height):
    return base*height*0.5
area = tri_area(10000,200)
print(area)
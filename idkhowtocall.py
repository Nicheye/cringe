x = int(input("x"))

savex= 0
small = 0
kr3 = 0
big = 0
while x!=0:
    
    if x%3==0:
        kr3=  x
        print("кратно трем",kr3)
    if savex and x%3==0>x:
        big =savex
        print("savex самый большой",savex)
    if x and x%3==0 >savex:
        big =x
        print("savex самый большой",x)    
    if x>savex and x%2==0:
        
        small=x
        print("x самый маленький",x)
    if savex<x and savex%2==0:
        small=savex
        print("savex самый маленький",savex)                 
    savex = x
    print(kr3+big+small)
    x=int(input("x"))

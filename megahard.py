x = int(input("x"))
fake=0
proiz=1
savex = 0
savex = x
while x<=1000000000:
    num1 = x//1
    
    if x>99:
        num1 = x//100
    if x>9:
        num1 = x//10
    if x>999:
        num1 = x//1000
    if x>9999:
        num1 = x//10000
    if x>99999:
        num1 = x//100000             
    
    while x<savex:
        
        savex = x
    
        
    
       
    print(savex,"savex")
    print("sum=",savex+num1)   
    x = int(input("x")) 
    

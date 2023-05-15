x = int(input("x"))

proiz=1

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
    numlast=x%10
    proiz= num1*numlast
        
    
    print(proiz,num1,numlast)    
    x = int(input("x"))

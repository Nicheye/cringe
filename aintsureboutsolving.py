x = int(input("x"))
sum=0
count = 0
while x<=30000:
    lastnum=x%10
    
    if lastnum!=3 and lastnum!=5 :
        sum = sum+x
        count=count+1
        
     
    
    x = int(input("x"))
print(sum/count) 

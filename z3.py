x = int(input("x"))
num1= x//100
num2 =(x//10)%10
num3= x%10

print("num1",num1)
print("num2",num2)
print("num3",num3)
if num1==num2==num3:
    print("все равны")
elif num1==num2:

    print("num1 = num2 ")
elif num1==num3:
    print("num1= num3")    
elif num2 == num3:
    print("num2 = num3")
else:
    print("никакие не равны")    



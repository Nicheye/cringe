x= int(input())
a= int(input())
num1 =x//1000
num2 = (x//100)%10
num3 = (x//10)%10
num4 = x%10
sum =num1+num2+num3+num4
proiz =num1*num2*num3*num4
print("num1",num1)
print("num2",num2)
print("num3",num3)
print("num4",num4)
if num1+num2==num3+num4:
    print("равны")
else:
    print("не равны")
if  sum %3 ==0:
    print("кратно 3")
else:
    print("не кратно 3")
if x%4 ==0:
    print("кратно 4")
else:
    print("не кратно 4")      
if x%a==0:
    print("кратно а")
else:
    print("не кратно")      

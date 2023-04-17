x = int(input("x"))
num1= x//10
num2= x%10
summacubov=(num1**3+num2**3)

if num2>num1:
    print('второе больше')
    print(x%10)
if num1 >num2:  
    print("первое больше")  
    print(x//10)

if x**2 == summacubov*0.25:
    print("равное")
    print(x**2,summacubov)
if x**2 != summacubov*0.25:
    print("не равно")
    print(x**2,summacubov)


num = int(input("введите число"))
countlastsymbol=0
count4 = 0
sum=0
proiz=1
count0=0
count5=0
for n in range(num):
    if n==3:
        print("в нем есть три")
    if n==num%10:
        countlastsymbol=countlastsymbol+1
    print("сколько раз встречает последяя цифра:",countlastsymbol)
    if n%2==0:
        count4=count4+1
    print("четное раз:",count4)
    if n>5:
        sum = sum+n
    print("cумма:",sum)
    if n>7:
        proiz = proiz*n
    print("произведение",proiz)    
    if n==0:
        count0= count0+1
    print("ноль встречается:",count0)
    if n==5:
        count5= count5+1
    print("пять встречается:",count5)
print("сколько раз встречает последяя цифра:",countlastsymbol,"четное раз:",count4,"cумма:",sum,"произведение",proiz,"ноль встречается:",count0,"пять встречается:",count5)

num = int(input("number"))
tryes = 0
count = int(input("how many yers"))
percent = int(input("how many percents"))
while tryes != count:
    tryes=tryes+1
    num = num + (num*percent//100)
    print(num)
     

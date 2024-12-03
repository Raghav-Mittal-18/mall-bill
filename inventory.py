name=[]
price=[]
quantity=[]
while True:
    command=int(input("press 1 to add,\npress 2 to remove,\npress 3 to calculate total vaue,\npress 4 to exit the list"))
    if command==1:
        na=input("enter the name of item:")
        pr=float(input("enter price of item:"))
        qu=float(input("enter the quantity of item:"))
        name.append([na,pr,qu])
        price.append(pr)
        quantity.append(qu)
    if command==2:
        na2=input("enter the name of item that you entered previously:")
        for i in name:
            if i[0]==na2:
                name.remove(i)
    sum=0
    if command==3:
        for i in name:
            sum+=(i[1]*i[2])
        print("your item list:",name)
        print("total bill is:",sum)
    if command==4:
        print("your item list , in the format of [item name, price, quantity]:",name)
        print("total bill is:",sum)
        break

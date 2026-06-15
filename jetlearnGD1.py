product = {"douzen eggs": 5,"milk": 4,"butter": 3,"bread": 6, "jam": 2}
for key,value in product.items():
    print(key,"is",value,"euro")
cart = {}
dubblebreak = True
while dubblebreak:
    item = input("What item do you want? ")
    if item not in product:
        print("Sorry, that is not in stock. ")
        continue
    times = int(input("and how many of those? "))
    cart[item] = times
    while True:
        cOntinue = input("Do you want to stop? ")
        if cOntinue == "yes" or cOntinue == "y":
            dubblebreak = False
            break
        elif cOntinue == "no" or cOntinue == "n":
            break
        else:
            print("please choose y/n")
            continue

for x,y in cart.items():
    calc = y * product[x]
    print(x,"x",y,calc,"euro") 
      

 
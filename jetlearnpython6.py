def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b 
def div(a,b):
    if b == 0:
        return "cannot divide by zero"
    return a / b
while True:
    print("option 1: additiom, option 2: subtraction, option 3, multiplication, option 4, division  option 5: exit")
    a = int(input("what do you need "))
    if a == 1:
        ans = int(input("what is the first number? "))
        ans2 = int(input("what is the second number? "))
        print(add(ans,ans2))
    elif a == 2:
        ans = int(input("what is the first number? "))
        ans2 = int(input("what is the second number? "))
        print(sub(ans,ans2))
    elif a == 3:
        ans = int(input("what is the first number? "))
        ans2 = int(input("what is the second number? "))
        print(mul(ans,ans2))
    elif a == 4:
        ans = int(input("what is the first number? "))
        ans2 = int(input("what is the second number? "))
        print(div(ans,ans2))
    elif a == 5:
        break
    else:
        print("please enter a number")
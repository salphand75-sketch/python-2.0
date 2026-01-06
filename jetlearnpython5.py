def square_number(ans):
    result = ans * ans
    print(result)

num = int(input("enter a number to square "))
square_number(num)

def vote(age):
    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not eligible")

age_input = int(input("Enter your age "))
vote(age_input)
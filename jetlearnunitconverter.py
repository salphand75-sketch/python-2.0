def k_to_m(ans):
    meters = ans * 1000
    return meters
def m_to_k(ans):
    kilo = ans / 1000
    return kilo
def c_to_m(ans):
    meters = ans / 1000
    return meters
def m_to_c(ans):
    kilo = ans / 1000
    return kilo
while True:

    print("option 1: kilometers to meters, option 2: meters to kilometers, option 3: centimeters to meters, option 4: meters to centimeters, option 5: exit")
    a = int(input("what do you need "))
    if a == 1:
        ans = int(input("what number "))
        print(k_to_m(ans))
    elif a == 2:
        ans = int(input("what number "))
        print(m_to_k(ans))
    elif a == 3:
        ans = int(input("what number "))
        print(c_to_m(ans))
    elif a == 4:
        ans = int(input("what number "))
        print(m_to_c(ans))
    elif a == 5:
        break
    else:
        print("please enter a number")
print("hi")
x = "Skye"
print(x)
y = int(input("what is your age "))
print(y)
if y > 12 and y < 18:
    print("you are a teenager ")
elif y >= 18:
    print("you are a adult ")
else:
    print("you are a kid ")    
for i in range(5):
    print(x)
z = ["hi","hello","yo","good morning"]
print(z[1])
z.append("good day")
print(z)
z.remove("hi")
print(z)
b = z.index("hello")
z[b] = "hey"
print(z)
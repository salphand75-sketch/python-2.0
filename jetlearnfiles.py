file = open("file.txt","w")
file.write("hello world this is my first file")
file.close()
file = open("file.txt","r")
file_to_the_power_of_2 = file.read()
print(file_to_the_power_of_2)
file.close()
file = open("file.txt","w")
file.write("hello world this is my second file")
file.close()
file = open("file.txt","a")
file.write(" \nhello world this is my third file")
file.close()
with open("file.txt","w") as file:
    file.write("hello world this is my fourth file")
with open("file.txt","a") as file:
    file.write(" \nhello world this is my fifth file")
with open("file.txt","r") as file:
    file_to_the_power_of_2 = file.readlines()
    print(file_to_the_power_of_2)
a = input("What do you need ")
with open("file.txt","w") as file:
    file.write(a)

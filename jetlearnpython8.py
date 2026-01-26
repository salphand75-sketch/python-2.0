grid = [["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"]]
import random
t_row = random.randint(0,4)
t_colum = random.randint(0,4)
t_row2 = random.randint(0,4)
t_colum2 = random.randint(0,4)
t_row3 = random.randint(0,4)
t_colum3 = random.randint(0,4)
while True:
    if t_row == 0 or t_colum == 0:
        t_row = random.randint(0,4)
        t_colum = random.randint(0,4)
    elif t_row2 == 0 or t_colum2 == 0:
        t_row2 = random.randint(0,4)
        t_colum2 = random.randint(0,4)
    elif t_row3 == 0 or t_colum3 == 0:
        t_row3 = random.randint(0,4)
        t_colum3 = random.randint(0,4)
    else:
        break
while True:
    if t_row == t_row2:
            t_row2 = random.randint(0,4)
    elif t_row2 == t_row3:
            t_row3 = random.randint(0,4)
    elif t_row3 == t_row:
            t_row3 = random.randint(0,4)
    elif t_colum == t_colum2:
            t_colum2 = random.randint(0,4)
    elif t_colum2 == t_colum3:
            t_colum3 = random.randint(0,4)
    elif t_colum3 == t_colum:
            t_colum3 = random.randint(0,4)
    else:
         break

for i in grid:
    for j in i:
        print(j, end = " ")
    print()
while True:
    ans_p_r = int(input("Which row do you think is safe "))
    ans_p_c = int(input("Which colum do you think is safe "))
    if ans_p_r == t_row and ans_p_c == t_colum or ans_p_r == t_row2 and ans_p_c == t_colum2 or ans_p_r == t_row3 and ans_p_c == t_colum3:
        print("You are dead")
        break
    else:
        print("You are safe...for now ")
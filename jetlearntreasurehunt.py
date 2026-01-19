grid = [["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"]]
import random
t_row = random.randint(0,4)
t_colum = random.randint(0,4)
for i in grid:
    for j in i:
        print(j, end = " ")
    print()
while True:
    ans_p_r = int(input("Which row you think the treasure is "))
    ans_p_c = int(input("Which colum you think the treasure is "))
    if ans_p_r == t_row and ans_p_c == t_colum:
        print("You got it right")
        break
    elif ans_p_r > t_row and ans_p_c == t_colum:
        print("guess a lower number for row ")
    elif ans_p_r < t_row and ans_p_c == t_colum:
        print("guess a higher number for row ")
    elif ans_p_c > t_colum and ans_p_r == t_row:
        print("guess a lower number for colum ")
    elif ans_p_c < t_colum and ans_p_r == t_row:
        print("guess a higher number for colum ")
    else:
        print("both the row and colum are incorect ")
grid = [["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"]]
import random
bomb = []
count = 0
while True:
     t_row = random.randint(0,4)
     t_colum = random.randint(0,4)
     if (t_row, t_colum) in bomb or (t_row, t_colum) == (0,0):
          continue
     bomb.append((t_row, t_colum))
     count += 1
     if count == 3:
          break
for i in grid:
    for j in i:
        print(j, end = " ")
    print()
moves =[]
while True:
    ans_p_r = int(input("Which row do you think is safe "))
    ans_p_c = int(input("Which colum do you think is safe "))
    if ans_p_r < 0 or ans_p_r > 4 or ans_p_c < 0 or ans_p_c > 4:
        print("invalid move! row and collum must be between 0 and 4")
        continue
    if (ans_p_r, ans_p_c) in moves:
        print("You already tried this move")
        continue
    moves.append((ans_p_r, ans_p_c))
    if (ans_p_r, ans_p_c) in bomb:
        print("You are dead")
        break
    else:
        print("You are safe...for now ")
    startr = ans_p_r -1
    endr = ans_p_r +2
    startc = ans_p_c -1
    endc = ans_p_c +2
    count = 0
    for row in range(startr,endr):
        for col in range(startc,endc):
            if(row,col) in bomb:
                count += 1
    print("you have",count,"bomb around")
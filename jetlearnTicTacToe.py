gridint = ["0","1","2","3","4","5","6","7","8"]
def grid():
    print(gridint[0],"|",gridint[1],"|",gridint[2])
    print("----------")
    print(gridint[3],"|",gridint[4],"|",gridint[5])
    print("----------")
    print(gridint[6],"|",gridint[7],"|",gridint[8])
def check_win():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for combo in winning_combinations:
        if gridint[combo[0]] == gridint[combo[1]] == gridint[combo[2]]:
            return True
    return False     
turn = "X"
turns = []
while True:
    grid()
    try: 
        position = int(input("Chose a position 0-8 "))
    except ValueError: 
        print("please only enter numbers between 0-8")
        continue
    if position in turns:
        print("Please choose a different position, already in use!")
        continue
    if position > 8 or position < 0:
        print("Please chose a valid position (between 0-8).")
        continue
    
    turns.append(position)
    gridint[position] = turn
    winner = check_win()
    if winner:
        grid()
        print("Player ",turn," wins")
        break
    if len(turns) == 9:
        grid()
        print("It's a tie!")
        break
    if turn == "X":
        turn = "O"
    elif turn == "O":
        turn = "X"
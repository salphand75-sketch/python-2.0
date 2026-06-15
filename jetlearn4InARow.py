grid = [[" " for i in range(7)] for j in range (6)]
def gridest():
    for i in range(6):
        print("|",end = "")
        for j in range(7):
            print (grid[i][j],"|",end = "")
        print()
        print("_"*22)
    print("  0  1  2  3  4  5  6")
def columcheck(colm):
    for i in range(5, -1, -1):
        if grid[i][colm] == " ":
            grid[i][colm] = turn
            return True
    return False
def wincheck():
    for i in range(6):
        for j in range(4):
            if grid[i][j] == grid[i][j + 1] == grid[i][j + 2] == grid[i][j + 3] == turn:
                return True
    for i in range(7):
        for j in range(3):
            if grid[j][i] == grid[j + 1][i] == grid[j + 2][i] == grid[j + 3][i] == turn:
                return True
    for i in range(3):
        for j in range(4):
            if grid[i][j] == grid[i + 1][j + 1] == grid[i + 2][j + 2] == grid[i + 3][j + 3] == turn:
                return True
    for i in range(3, 6):
        for j in range(4):
            if grid[i][j] == grid[i - 1][j + 1] == grid[i - 2][j + 2] == grid[i - 3][j + 3] == turn:
                return True
    return False
def tiecheck():
    for row in grid:
        if " " in row:
            return False
    return True
turn = "X"
while True:
    gridest()
    try:
        col = int(input(f"Player {turn}, choose a column (0-6): "))
        if col < 0 or col > 6:
            print("Invalid column! Please choose between 0 and 6.")
            continue
    except ValueError:
        print("Choose a number!")
        continue
    if columcheck(col) == False:
        print("This column is full, please choose a different column.")
        continue        
    if wincheck():
        gridest()  
        print(f"Player {turn} wins!")
        break       
    if tiecheck():
        gridest()  
        print("It's a tie game!")
        break       
    if turn == "X":
        turn = "O"
    elif turn == "O":
        turn = "X"

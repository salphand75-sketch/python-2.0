grid = [[" " for i in range(7)] for j in range (6)]
def gridest():
    for i in range(6):
        print("|",end = "")
        for j in range(7):
            print (grid[i][j],"|",end = "")
        print()
        print("_"*22)
gridest()
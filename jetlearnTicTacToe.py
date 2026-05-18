gridint = ["0","1","2","3","4","5","6","7","8"]
def grid():
    print(gridint[0],"|",gridint[1],"|",gridint[2])
    print("----------")
    print(gridint[3],"|",gridint[4],"|",gridint[5])
    print("----------")
    print(gridint[6],"|",gridint[7],"|",gridint[8])
turn = "X"
turns = []
while True:
    grid()
    position = int(input("Chose a position 0-8 "))
    if position in turns:
        print("Please choose a different position, already in use!")
        continue
    turns.append(position)
    gridint[position] = turn
    if turn == "X":
        turn = "O"
    elif turn == "O":
        turn = "X"
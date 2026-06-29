box = [[0,9,2],[3,5,7],[8,1,6]]
yes = 0
for i in range(3):
    magic = 0
    for j in range(3):
        print(box[i][j],end=" ")
        magic += box[i][j]
    print("","=",magic)
    if magic == 15:
        yes += 1
for k in range(3):
    magic = 0
    for l in range(3):
        print(box[l][k],end=" ")
        magic += box[l][k]        
    print("","=",magic)
    if magic == 15:
        yes += 1
magic = 0
for m in range(3):

    print(box[m][m],end=" ")
    magic += box[m][m]
print("","=",magic)
if magic == 15:
    yes += 1

magic = 0
for n in range(3): 
    for o in range(2-n,3-n):
        print(box[n][o],end=" ")
        magic += box[n][o]
print("","=",magic)
if magic == 15:
    yes += 1

if yes == 8:
    print("Its a magic box!")
else:
    print("It's not a magic box :(")
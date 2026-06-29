numbers = [[1,2],[3,4],[5,6]]
print(numbers)
for i in range(2,-1,-1):
    sum = 0
    for j in range(2):
        print(numbers[i][j],end=" ")
        sum += numbers[i][j]
    print("",sum)

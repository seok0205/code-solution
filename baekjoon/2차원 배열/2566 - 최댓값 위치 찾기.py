arr1 = []
maxnum = 0
maxrow, maxcol = 0, 0

for i in range(9):
    i = list(map(int, input().split()))
    arr1.append(i)

for i in range(9):
    for j in range(9):
        if arr1[i][j] >= maxnum:
            maxnum = arr1[i][j]
            maxrow = i + 1
            maxcol = j + 1

print(maxnum)
print(maxrow, maxcol)
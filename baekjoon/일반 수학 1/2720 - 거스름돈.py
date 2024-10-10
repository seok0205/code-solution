T = int(input())
result = [[0 for i in range(4)] for j in range(T)]

for i in range(T):
    C = int(input())
    result[i][0] = C // 25
    C = C % 25
    result[i][1] = C // 10
    C = C % 10
    result[i][2] = C // 5
    C = C % 5
    result[i][3] = C

for i in result:
    for j in i:
       print(j, end=' ')
    print()
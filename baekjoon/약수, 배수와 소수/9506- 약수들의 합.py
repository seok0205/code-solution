n = []

while 1:
    a = int(input())
    n.append(a)
    if a == -1:
        break

number = [[] for i in range(len(n)-1)]

for i in range(len(n)-1):
    for j in range(n[i]):
        if n[i] % (j+1) == 0:
            number[i].append(j+1)

result = [[] for i in range(len(n)-1)]

for i in range(len(number)):
    if sum(number[i][:-1]) == n[i]:
        result[i].append(str(n[i]) + " = 1")
        for j in range(len(number[i])-2):
            result[i].append(" + " + str(number[i][j+1]))
    else:
        result[i].append(str(n[i]) + " is NOT perfect.")

for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j], end='')
    print()
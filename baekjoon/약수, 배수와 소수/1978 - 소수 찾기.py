N = int(input())
num = input().split()

result = 0

for i in range(N):
    a = 0
    for j in range(int(num[i])):
        if int(num[i]) % (j + 1) == 0:
            a += 1
    if a == 2:
        result += 1

print(result)
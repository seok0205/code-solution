M = int(input())
N = int(input())

result = []

for i in range(M, N+1):
    a = 0
    for j in range(1, i+1):
        if i % j == 0:
            a += 1
    if a == 2:
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))
N, K = map(int, input().split())
number = []

for i in range(N+1):
    if N % (i+1) == 0:
        number.append(i+1)

if len(number) <= K-1:
    print(0)
else:
    print(number[K-1])
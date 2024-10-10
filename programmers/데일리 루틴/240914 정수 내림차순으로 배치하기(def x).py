n = list(input())

n.sort()
n.reverse()

for i in range(len(n)):
    print(n[i], end='')
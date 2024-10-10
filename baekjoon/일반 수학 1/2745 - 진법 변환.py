N, B = input().split()

change = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N = N[::-1]
result = 0

for i in range(len(N)):
    n = str(N[i])
    result += (int(B)**i) * (change.index(n))

print(result)

#n, b = map(str, input().split())
#print(int(n,int(b)))
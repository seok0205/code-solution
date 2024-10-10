N = int(input())
a = 2
result = 4

for i in range(N):
    a = a + (a -1)
    result = a**2

print(result)
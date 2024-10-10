N = int(input())
num = 1
result = 1

while N > num:
    num += 6 * result
    result += 1

print(result)
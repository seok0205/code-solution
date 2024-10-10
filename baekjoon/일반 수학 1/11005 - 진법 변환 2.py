N, B = map(int, input().split())
result = ""
change = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while N != 0:
    result = change[N % B] + result
    N //= B

print(result)
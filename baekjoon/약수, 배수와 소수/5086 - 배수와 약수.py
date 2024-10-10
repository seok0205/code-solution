result = []

while True:
    A, B = map(int, input().split())

    if A == 0 and B == 0:
        break

    if A <= B and B % A == 0:
        result.append("factor")
    elif A >= B and A % B == 0:
        result.append("multiple")
    else:
        result.append("neither")

for i in range(len(result)):
    print(result[i])
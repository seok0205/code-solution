x_point = []
y_point = []
result = [0, 0]

for i in range(3):
    a, b = map(int, input().split())
    x_point.append(a)
    y_point.append(b)

for i in range(3):
    if x_point.count(x_point[i]) == 1:
        result[0] = x_point[i]
    elif y_point.count(y_point[i]) == 1:
        result[1] = y_point[i]

print(result[0], result[1])
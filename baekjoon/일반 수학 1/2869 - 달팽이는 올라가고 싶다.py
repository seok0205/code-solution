A, B, V = map(int, input().split())
day = 0

day = (V - B) / (A - B)

if day - int(day) > 0.0:
    day = day + 1

print(int(day))
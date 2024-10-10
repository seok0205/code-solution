a = int(input())
arr1 = [[0] * 100 for i in range(100)]

for i in range(a):
    l, h = map(int, input().split())
    for j in range(l, l+10):
        for k in range(h, h+10):
            arr1[j][k] = 1

width = 0
for i in arr1:
    width += sum(i)

print(width)
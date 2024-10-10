arr1 = []
result = ""

for i in range(5):
    i = list(input())
    arr1.append(i)

max_length = max(len(i) for i in arr1)

for a in range(max_length):
    for b in range(5):
        if a < len(arr1[b]):
            result += arr1[b][a]

print(result)
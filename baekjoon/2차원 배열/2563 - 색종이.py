'''
2563 S5 색종이

가로, 세로 크기 100인 정사각형 모양흰색 도화지 존재.
이 도화지 위에 가로세로 10인 정사각형의 검은색 색종이를 색종이 변과 도화지 변이 평행하도록 붙임
이러한 방식으로 색종이를 한 장 혹은 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 문제
'''

a = int(input())
arr1 = [[0] * 100 for _ in range(100)]

for i in range(a):
    l, h = map(int, input().split())
    for j in range(l, l+10):            # 검은 색종이 붙이기 10x10의 범위에.
        for k in range(h, h+10):
            arr1[j][k] = 1      # 덮인 부분은 1로 표현

width = 0
for i in arr1:          # 해당 부분이 1인 부분의 개수가 곧 검은 색종이의 넓이
    width += sum(i)

print(width)
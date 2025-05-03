'''
S5 11650 좌표 정렬하기

2차원 평면 위에 점 N개 주어짐.
좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

N = int(input())
location = list()

for _ in range(N):
    x, y = map(int, input().split())

    location.append((x, y))         # 입력받고 좌표리스트에 추가

location.sort(key=lambda x: x[1])       # 먼저 y좌표 순서대로 나열한 후,
location.sort()                         # x좌표 큰 순서로 다시 나열하면, 문제 조건 만족.

for i in location:          # 출력
    print(i[0], i[1])
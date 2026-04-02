'''
B2 25558 내비게이션

문제 설명:
N개의 데이터는 아래와 같이 이루어짐
1. 시작점과 도착점
2. 각 내비게이션 시작점에서 도착점 까지 도달하기 위해 순차적으로 방문해야하는 중간 지점들의 위치

두 지점간 거리는 맨해튼 거리로 정의.
abs(a-c) + abs(b-d).
각 내비게이션이 안내한 목적지까지 최적 경로는 서로 다름.

최소 거리 담은 데이터 찾기.

입력:
첫줄 - 내비게이션 개수 N (2 <= N <= 1000)
두번째 줄 - 좌표값 sx, sy, ex, ey(시작, 도착점 좌표) 각 -10**9보다 크고 10**9보다 작음.
다음 줄 부터 N번 내비게이션까지의 데이터가 입력됨.
- 첫줄 - 순차적 방문 중간 지점 위치 개수 M(1 <= M <= 100)
- 두 번째 줄 - M개의 줄에 걸쳐 j번째로 방문해야하는 중간 지점 (x, y) 주어짐.(정수)

출력:
최적의 거리 데이터 담은 번호 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N = int(input())
sx, sy, ex, ey = map(int, input().split())
result = []
for _ in range(N):
    M = int(input())
    i = sx
    j = sy
    dist = 0
    for _ in range(M):
        x, y = map(int, input().split())

        dist += (abs(x-i) + abs(y-j))

        i, j = x, y

    dist += (abs(i-ex) + abs(j-ey))

    result.append(dist)

print(result.index(min(result))+1)
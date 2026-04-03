'''
G3 31248 3+1 하노이 탑

문제 설명:
3+1 하노이 탑 게임은 가로 방향으로 일렬로 놓인 4개의 기둥과 크기가 서로 다른 N개의 원판을 이용한 게임.
편의상 왼쪽 기둥부터 차례로 A, B, C, D라 함.
처음에는 기둥 A에 크기가 가장 큰 원판이 아래로 오도록 모든 원판이 크기 순서대로 쌓여 있음.
이 게임 목표는 규칙을 지키면서 모든 원판을 기둥 D로 옮기는 것.

1. 한번에 1개 원판만 옮길 수 있음.
2. 어떤 기둥의 맨 위에 있는 원판만 옮길 수 있음.
3. 작은 원판 위에 큰 원판을 놓을 수 없음.
4. 기둥 D에 있는 원판을 다른 기둥으로 옮길 수 없음.
5. 기둥 A, B, C에 있는 원판은 위 조건을 어기지 않는 한 자유롭게 옮길 수 있음.

기둥 A에 있는 N개의 원판을 모두 기둥 D로 옮기기 위해 필요한 최소 이동 횟수 구하고, 이동 방법을 아무거나 출력.

입력:
정수 N.(1 <= N <= 20)

출력:
첫 번째 줄에 원판을 모두 옮기기 위해 필요한 최소 이동 횟수 M 출력.
다음 줄 부터 M줄에 걸쳐 원판 이동을 하나씩 출력. 원판을 기둥 X에서 기둥 Y로 옮겼을 때, 'x y' 형태로 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N = int(input())
route = []

def hanoi(n, s, e, mid):
    if n == 0:
        return
    if n == 1:
        route.append((s, e))
        return
    
    hanoi(n-1, s, mid, e)
    route.append((s, e))
    hanoi(n-1, mid, e, s)
    

def recursion(n, a, b, c, d):
    if n == 0:
        return
    if n == 1:
        route.append((a, d))
        return
    
    hanoi(n-2, a, b, c)
    route.append((a, c))
    route.append((a, d))
    route.append((c, d))

    recursion(n-2, b, a, c, d)


recursion(N, 'A', 'B', 'C', 'D')

print(len(route))
for data in route:
    print(data[0], data[1])
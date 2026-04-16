'''
G5 2493 탑

문제 설명:
일직선 위에 N개의 높이가 서로 다른 탑을 수평 직선의 왼쪽부터 오른쪽 방향으로 차례로 세우고, 꼭대기에 레이저 송신기 설치.
모든 탑의 레이저 송신기는 레이저 신호를 지표면과 평행하게 수평 직선의 왼쪽 방향으로 발사하고, 탑의 기둥 모두에는 레이저 신호를 수신하는 장치가 설치되어 있음.
하나의 탑에서 발사된 레이저 신호는 가장 먼저 만나는 단 하나의 탑에서만 수신이 가능.

탑들의 개수 N과 탑들의 높이가 주어질 때, 각각의 탑에서 바사한 레이저 신호를 어느 탑에서 수신하는지를 알아내는 프로그램을 작성하라.

입력:
첫째 줄 - 탑의 수 N (1 <= N <= 500,000)
둘째 줄 - N개의 탑들의 높이가 직선상에 놓인 순서대로 하나의 빈칸을 사이에 두고 주어짐.
탑들의 높이는 1이상 100,000,000이하의 정수.

출력:
첫째 줄에 주어진 탑들의 순서대로 각각의 탑들이 발사한 레이저 신호를 수신한 탑들의 번호를 하나의 빈칸을 사이에 두고 출력.
만약 신호를 수신하는 탑이 존재하지 않으면 0 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))
stack = []
result = []

if N == 1:
    print(0)
else:
    for i in range(N):
        now = towers[i]

        while stack and stack[-1][1] < now:
            stack.pop()
        
        if not stack:
            result.append(0)
        else:
            result.append(stack[-1][0])
        
        stack.append((i + 1, now))
            

    print(' '.join(map(str, result)))
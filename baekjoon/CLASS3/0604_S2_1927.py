'''
S2 1927 최소 힙

자료 구조 최소 힙
1. 배열에 자연수 x 넣기
2. 배열에서 가장 작은 값 출력, 그 값을 배열에서 제거

비어있는 배열에서 시작
0은 2번 기능.
정수 x는 1번 기능을 뜻하는 연산.
음의 정수는 입력 안됨
'''

import sys
# sys.stdin = open('tc.txt', 'r')

import heapq
input = sys.stdin.readline

N = int(input())
hq = []                 # 최소힙 리스트

for _ in range(N):
    num = int(input())

    if num == 0:            # 입력 받은 숫자 0이면 힙 비어있는지 확인 후,
        if len(hq):
            print(heapq.heappop(hq))        # 작은 수 꺼내고 출력
        else:               # 비어있으면 0 출력
            print(0)
    else:
        heapq.heappush(hq, num)     # 입력받은 숫자를 힙에 푸시

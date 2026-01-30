'''
G4 7662 이중 우선순위 큐

문제 설명:
전형적인 큐와 차이점은 데이터를 삭제할 때, 연산 명령에 따라 우선순위가 가장 높은 데이터 또는 가장 데이터 중 하나를 삭제하는 것.
이중 우선순위 큐는 두가지 연산 사용됨.
하나는 데이터를 삽입하는 연산, 하나는 데이터를 삭제하는 연산.
데이터를 삭제하는 연산은 두 가지 종류가 있음.
하나는 우선순위가 가장 높은 것을 삭제, 하나는 우선순위가 가장 낮은 것을 삭제.
Q에 적용될 일련의 연산이 주어질 때 이를 처리한 후 최종적으로 Q에 저장된 데이터 중 최댓값과 최솟값을 출력하는 문제

입력:
첫째 줄 - T
T의 첫째 줄 - Q에 적용할 연산 개수 k (~1,000,000)
이어지는 k줄 - 연산을 나타내는 문자 (D or I), 정수 n(I n은 정수 n을 Q에 삽입하는 연산)
D -1은 최솟값을 삭제하는 연산 의미.
최댓값 및 최솟값을 삭제하는 연산에서 최대최솟값이 둘 이상이면, 하나만 삭제.
만약 Q가 비어있는데 적용할 연산이 D라면 무시.
Q에 저장될 모든 정수는 -2**31 이상 2**31 미만인 정수

출력:
각TC에 대해 모든 연산 처리한 후 Q에 남아 있는 값 중 최댓값과 최솟값을 출력.
두 값은 한 줄에 출력하되 하나의 공백으로 구분.
만약 Q가 비어있다면 'EMPTY' 출력
'''

import sys
import heapq
sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

T = int(input())

for _ in range(T):
    k = int(input())
    max_q = []
    min_q = []
    visit = [False] * k
    cnt = 0

    for i in range(k):
        command, n = map(str, input().strip().split())
        
        if command == 'I':
            cnt += 1
            heapq.heappush(min_q, (int(n), i))
            heapq.heappush(max_q, (-int(n), i))
        elif command == 'D' and min_q and max_q:
            if n == '1':
                while max_q:
                    a = heapq.heappop(max_q)
                    if visit[a[1]] == False:
                        visit[a[1]] = True
                        break
            elif n == '-1':
                while min_q:
                    a = heapq.heappop(min_q)
                    if visit[a[1]] == False:
                        visit[a[1]] = True
                        break
    
    while max_q and visit[max_q[0][1]]:
        heapq.heappop(max_q)

    while min_q and visit[min_q[0][1]]:
        heapq.heappop(min_q)

    if max_q and min_q:
        output(str(-max_q[0][0]) + ' ' + str(min_q[0][0]) + '\n')
    else:
        output('EMPTY' + '\n')
'''
D3 17014 연산

자연수 N에 몇 번의 연산이 +1, -1, *2, -10 네 가지라고 할 때 최소 몇 번의 연산을 거쳐야 하는지 알아내는 문제
단, 연산의 중간 결과도 항상 백만 이하의 자연수여야 함

예로, N=2, M=7인 경우, (2+1)*2+1 = 7 이므로 최소 3번의 연산이 필요함
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

from collections import deque


def bfs(s):
    q = deque()
    visit = [0] * 1000001           # 연산 중 나오는 수와 같은 인덱스에 방문 표시를 할 것
    q.append(s)                     # 시작 숫자
    visit[s] = 1
    
    while True:
        a = q.popleft()
        
        for k in range(4):          # 0부터 3까지 '+1', '-1', '*2', '-10' 차례로 연산
            if a > M and (k == 0 or k == 2):
                continue
            
            if k == 0:
                sub = a + 1
            elif k == 1:
                sub = a - 1
            elif k == 2:
                sub = a * 2
            elif k == 3:
                sub = a - 10
                
            if sub == M:            # 똑같은 수 찾아내면 해당 숫자 인덱스에 들어있는 값 반환(연산 횟수와 같음)
                return visit[a]
            if sub <= 1000000 and not visit[sub]:       # 백만보다 작고 한번도 보지 못한 숫자면 연산 횟수 집어넣고, 인큐
                visit[sub] = visit[a] + 1
                q.append(sub)


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    
    result = bfs(N)
    
    print(f'#{tc} {result}')
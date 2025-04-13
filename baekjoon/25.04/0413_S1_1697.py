'''
S1 1697 숨바꼭질

숨바꼭질 중. 나는 현재 N(0이상 100,000 이하)에 있고, 다른 사람은 점 K(0이상 100,000이하)에 있음.
난 걷거나 순간이동 가능. 내가 위치가 X일 때 걷는다면 1초 후에 X-1 혹은 X+1로 이동하게 됨.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 됨

나와 다른 사람의 위치가 주어질때, 내가 다른사람을 찾을 수 있는 가장 빠른 시간이 몇초인지 구하는 문제
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

from collections import deque


def hide_and_seek(x):
    global result

    q = deque()
    q.append(x)
    visit = [0] * 100001
    visit[x] = 1

    while q:
        target = q.popleft()
        if target == K:             # 꺼내온 위치가 K랑 같으면 result 바꾸고 함수 종료
            result = visit[target] - 1
            return

        record = []                 # x*2, x-1, x+1 리스트에 넣고 돌아가며 계산 후 조건 맞으면 인큐
        record.extend([target * 2, target + 1, target - 1])

        for a in record:
            if a > 100000 or a < 0:     # 범위넘어가거나 이미 방문했으면 다음 위치 탐색
                continue

            if visit[a]:
                continue

            visit[a] = visit[target] + 1        # 이전 위치의 시간에 1초더하기
            q.append(a)
        
        record = []


N, K = map(int, input().split())
record = []
result = 0

hide_and_seek(N)

print(result)
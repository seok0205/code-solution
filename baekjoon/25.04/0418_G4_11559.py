'''
G4 11559 Puyo Puyo

뿌요뿌요의 룰:
필드에 여러 가지 색깔의 뿌요를 놓는다. 뿌요는 중력의 영향을 받아 아래 바닥이나
다른 뿌요가 나올 때까지 아래로 떨어짐.
뿌요 놓고 난 후, 같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 연결된 같은 색 뿌요가 한번에 없어짐.
이때 1연쇄 시작.
아래로 떨어지고 나서 다시 같은 색의 뿌요들이 4개 이상 모이면 또 터짐. 터진 후 뿌요들이 내려오고 다시 터짐을 반복할 때마다 1연쇄씩 늘어남.
터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야 하고 여러 그룹이 터지더라도 한번의 연쇄가 추가.

필드가 주어졌을 때, 연쇄가 몇 번 연속으로 일어날 지 계산하는 문제.

입력:
12개의 줄에 필드 정보가 주어짐. 각 줄에는 6개의 문자 존재.
'.'은 빈공간, '.'이 아니면 각각 색깔의 뿌요를 나타냄.
R 빨강, G 초록, B 파랑, P 보라, Y 노랑

전부 아래로 떨어진 뒤의 상태임. 뿌요 아래에 빈칸이 있는 경우 없음.

출력:
연쇄가 몇번인지 출력. 하나도 터지지 않으면 0 출력.
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

from collections import deque

def find_chain(a, b, color, field):         # 같은 색 공 찾기
    global cnt

    new_field = [i[:] for i in field]       # field 깊은 복사. 만약 공이 4개 안모여서 안터지면 이전 맵 field를 그대로 써야함

    q = deque()
    q.append((a, b))
    visit[a][b] = 1             # 하나의 턴에는 같은 공끼리만 방문할 것이므로 visit를 같이 써도 상관 없음
    new_field[a][b] = '.'       # 공이 터질 수 있는 조건이면 new_field의 공을 '.'으로 만듦
    cnt += 1                    # 중앙에 있는 공부터 세야함.

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]

            if nx < 0 or nx >= 12 or ny < 0 or ny >= 6:     # 맵 안이고,
                continue

            if visit[nx][ny]:           # 방문 안한 곳이고,
                continue

            if new_field[nx][ny] != color:      # 색깔도 같다면,
                continue

            q.append((nx, ny))          # 다음 탐색 대상이므로 인큐
            new_field[nx][ny] = '.'     # 공을 터트려주고
            visit[nx][ny] = 1           # 방문 표시까지 해줌
            cnt += 1                    # 터진 공에 추가

    return new_field        # 공이 터진 상태의 필드를 반환


def puyo_set():         # 한턴이 지났을 때, 공을 밑으로 내리는 함수
    for a in range(6):
        for b in range(11, 0, -1):
            if field[b][a] == '.':
                for c in range(b-1, -1, -1):
                    if field[c][a] in ['R', 'G', 'B', 'P', 'Y']:
                        field[b][a], field[c][a] = field[c][a], field[b][a]
                        break


field = [list(input()) for _ in range(12)]      # 필드 입력
result = 0                                      # 연쇄가 몇번 일어났는가?

di = [0, 0, 1, -1]      # 델타 활용
dj = [1, -1, 0, 0]

while True:
    chain = 0           # 한 턴에 일어난 연쇄 횟수
    visit = [[0] * 6 for _ in range(12)]        # 한턴에 쓸 방문 리스트

    for i in range(12):         # 맵을 순회하며
        for j in range(6):
            cnt = 0             # 공이 터진 개수
            if visit[i][j] == 0 and field[i][j] in ['R', 'G', 'B', 'P', 'Y']:       # 만약 방문 안한 공이고, 색깔이 있는 공이면, 4개 이상 연결되있는지 확인해야함!
                new_field = find_chain(i, j, field[i][j], field)

            if cnt > 3:         # 만약 공이 4개 이상 터졌다??
                chain += 1          # 연쇄 횟수 1 증가
                field = new_field       # 공이 터진 상태의 new_field를 공이 터지기 전 상태인 field와 대체. 만약 공이 4개 이상 안터지면 기존 field로 유지됨.
                
    if chain:       # 만약 공이 터진 현상이 일어났다?
        result += 1     # 연쇄 횟수 1 이상이라도 어차피 1회로 간주. 결과값 1 증가.
        puyo_set()      # 공이 터졌으니 위의 공 내리기
    else:           # 만약 공이 터진 현상이 끊겼다?
        break           # 중단하고 결과 출력!

print(result)
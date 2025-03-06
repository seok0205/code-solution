'''
D4 10966 물놀이를 가자

NxM 격자로 표현 가능. 위쪽에서 i번째 줄의 왼쪽에서 j번째 칸이 물이 되면 W, 땅이면 L로 표현
어떤 칸에 사람이 있으면, 그 칸의 상하좌우에 있는 칸으로 이동하는 것을 반복해 다른 칸으로 이동 가능
격자 밖으로 나가는 이동은 불가능
땅으로 표현된 모든 칸에 대해서 어떤 물인 칸으로 이동하기 위한 최소 이동 횟수 구하고, 모든 이동 횟수의 합 출력

시간이 빡빡함. 1000x1000, 1,000,000
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


from collections import deque                

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    
    visit = [[-1] * M for _ in range(N)]
    
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    
    q = deque()
    for i in range(N):
        field = input()
        for j in range(M):
            if field[j] == 'W':     # 입력받은 중 물가면 인덱스를 큐에 추가.
                q.append((i, j))
                visit[i][j] = 0     # 물가는 visit의 해당되는 부분 0으로 지정
    
    while q:
        location = q.popleft()      # 물가 하나씩 디큐
        for k in range(4):
            x = location[0] + di[k]
            y = location[1] + dj[k]
            
            if x < 0 or x >= N or y < 0 or y >= M:      # 4방향 보면서 배열 밖이면 돌아감
                continue
                
            if visit[x][y] != -1:       # -1이 아니면 돌아감(방문했거나, 물가임)
                continue
            
            q.append((x, y))        # 위조건을 통과하면 방문안한 땅이므로 인큐
            visit[x][y] = visit[location[0]][location[1]] + 1       # 현재 노드의 +1된 값을 대입
    
    result = 0
    for i in visit:     # visit에 담긴 모든 수 더하면 총 모든땅 거리(땅을 지나간(밟은) 수랑 같으므로)
        for j in i:
            result += j
    
    print(f'#{tc} {result}')
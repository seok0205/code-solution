'''
모의 SW 역량테스트 5656 벽돌 깨기

구슬을 쏘아 벽돌을 깨뜨리는 게임
구슬은 N번 쏠수 있고, 벽돌은 WxH 배열로 주어짐

규칙:
1. 구슬은 좌, 우로만 움직일 수 있어 항상 맨 위에 있는 벽돌만 깨뜨릴 수 있음
2. 벽돌은 숫자 1~9로 표현, 구슬이 명중한 벽돌은 상하좌우(벽돌에 적힌 숫자 - 1)칸 만큼 같이 제거

주어진 구슬을 N번 쐈을때, 남은 벽돌의 개수를 구하는 문제
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

from collections import deque


def map_set(cnt, remains, bricks):
    global result
    
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    
    if cnt == N or remains == 0:        # 재귀함수 탈출 조건(벽돌 부순 횟수가 N번이거나 남은 벽돌이 없을 때)
        result = min(result, remains)   # 남은 벽돌 수와 전역변수 result 비교 후 작은거 대입
        return
    
    for i in range(W):      # 열 탐색
        sub_bricks = [arr[:] for arr in bricks]     # 얕은 복사 방지
        
        for j in range(H):
            if sub_bricks[j][i]:            # 깰 수 있는 벽돌 발견하면 변수 만듦
                brick = (j, i, sub_bricks[j][i])        # 좌표와, 블록안의 숫자를 기억
                break
        else:           # 해당 열에서 깰수 있는 벽돌 발견 실패 시, 다음 열로 이동
            continue
            
        q = deque()
        q.append((brick[0], brick[1], brick[2]))        # 큐에 부술 벽돌 좌표와 폭발 범위 인큐
        now_remains = remains - 1                       # 하나는 무조건 부수므로, 남은 벽돌에서 1 감소
        sub_bricks[brick[0]][brick[1]] = 0
        
        while q:            # 폭발로 인해 터지는 범위 구하기
            target = q.popleft()
            
            for k in range(1, target[2]):       # 델타를 활용해서 블록에 담긴 폭발 범위 구함
                for m in range(4):
                    x = target[0] + (di[m] * k)
                    y = target[1] + (dj[m] * k)
                    if 0 <= x < H and 0 <= y < W and sub_bricks[x][y]:      # 만약 배열 안에 있고, 해당 블록이 0이아니면(안 터진 블록이 있따면)
                        q.append((x, y, sub_bricks[x][y]))          # 좌표, 폭발 범위 인큐
                        sub_bricks[x][y] = 0        # 해당 좌표는 터지므로 0 값 입력
                        now_remains -= 1            # 하나 터져서 1 감소
                    
        for a in range(W):      # 이어서 터지고 남은 블록 내리기
            top_brick = H-1     # 하나의 블록 고정 시켜놓고
            for b in range(top_brick, -1, -1):      # 위에 남아있는 블록을 발견하면 고정시킨 블록과 자리 변경.
                if sub_bricks[b][a]:
                    sub_bricks[b][a], sub_bricks[top_brick][a] = sub_bricks[top_brick][a], sub_bricks[b][a]
                    top_brick -= 1      # 한번 바꾸면 고정 시켜놓은 블록의 열 좌표 1 감소(위로 올라감, 시작이 맨 밑이기 때문)

        map_set(cnt + 1, now_remains, sub_bricks)   # 재귀함수


T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]
    
    result = float("inf")       # 최솟값 구하므로 inf 활용
    not_boom = 0
    
    for i in bricks:    # 총 벽돌 구하기
        for j in i:
            if j:
                not_boom += 1
    
    map_set(0, not_boom, bricks)        # 함수 실행
    
    print(f'#{tc} {result}')

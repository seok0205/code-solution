'''
G3 15684 사다리 조작

사다리 게임은 N개의 세로선(초록선), M개의 가로선(점선)으로 이루어짐.
인접한 세로 선사이에는 가로선 놓을 수 있음. 각각 세로선마다 가로선 놓을 수 있는 위치의 개수는 H.
모든 세로선이 같은 위치 가짐.

가로선은 인접 두 세로선을 연결해야 하지만 두 가로선이 연속하거나 접하면 안 됨.
점선 위에 있어야함.

사다리에 가로선을 추가해 결과 조작하려고함.
i번 세로선의 결과가 i번이 나와야 함. 추가해야하는 가로선 개수 최솟값 구하는 문제

입력:
첫 줄 - N, M, H (가로, 세로, 세로선마다 가로선 놓을 수 있는 위치 개수)
M줄 동안 가로선의 정보 주어짐(a, b: b번 세로선 b+1번 세로선을 a번 점선 위치에서 연결)
가장 위 점선 번호는 1번. 세로선은 왼쪽에 있는 것이 1번.
입력에 연속 가로선은 없음.

출력:
추가해야하는 가로선 개수 최솟값.
만약 정답이 3보다 크면 -1 출력. 불가능해도 -1 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline


def check():                # 각 i번째 출발점이 i번째 끝점과 이어져있는지 확인 
    di = [1, -1]
    for i in range(N):      # N개줄 모두 확인
        N_location = i
        idx = 0

        while True:
            if idx == H:        # 만약 끝까지 내려갔는데
                if N_location == i:     # 출발점 끝점이 같다?
                    break               # 다음 사다리 확인하러 break
                else:           # 맞지 않으면 그대로 종료 후 False 반환
                    return False
            
            if ladder[idx][N_location] != 0:        # 0이 아니면 사다리가 있단 뜻 
                for k in range(2):                  # 양 옆 확인후 이어져있는 곳으로 이동
                    x = N_location + di[k]

                    if x < 0 or x >= N or idx < 0 or idx >= H:
                        continue

                    if ladder[idx][N_location] == ladder[idx][x]:   # 사다리의 숫자같아야 이어져있는 곳임
                        N_location = x
                        idx += 1
                        break
            else:       # 0이면 그대로 내려감
                idx += 1
    else:           # False 반환하지 않고 쭉 for문 이행하면 True 반환
        return True


def make_result(cnt):
    global result, num

    if cnt >= result:       # result보다 cnt가 커지만 최솟값 구할수 없음.
        return

    if cnt == 3:            # 완벽한 사다리라도 사다리 설치 개수 3 초과면 -1출력이라 3번까지만 찾아보고 탈출
        if check():
            result = min(result, cnt)
        return
        
    if check():             # cnt 3이안된 상태면 사다리 추가할 때마다 체크해줌.
        result = min(result, cnt)
        return
    
    for j in range(N-1):        # 사다리 하나씩 추가해서 dfs 재귀 활용
        for i in range(H):
            if ladder[i][j] == 0 and ladder[i][j+1] == 0:
                ladder[i][j], ladder[i][j+1] = num, num     # 이어져있는 사다리 구분하려 각 추가마다 1추가한 숫자 배열에 대입
                num += 1
                make_result(cnt+1)
                ladder[i][j], ladder[i][j+1] = 0, 0


N, M, H = map(int, input().split())
ladder = [[0] * N for _ in range(H)]

num = 1

for _ in range(M):          # 사다리 초기 상태 생성
    garo_a, garo_b = map(int, input().split())

    ladder[garo_a-1][garo_b-1] = num
    ladder[garo_a-1][garo_b] = num

    num += 1

result = 5      # 어차피 3 초과. 4부터는 -1로 출력.
make_result(0)

if result == 5:     # 게다가 5가 바뀌지 않는다는 것도 맞출 가능성 없거나 그이상이라는 뜻 cnt는 3에서 끊기기 때문
    print(-1)
else:
    print(result)
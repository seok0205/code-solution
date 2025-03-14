'''
모의 SW 역량테스트 2105 디저트 카페

길이 N인 정사각형 모양 가진 지역에 디저트 카페 밀집
원 안의 숫자는 해당 디저트 카페에서 팔고 있는 디저트 종류 의미,
카페들 사이에는 대각선 방향으로 움직일 수 있는 길 존재
디저트 카페 투어는 어느 한 카페에서 출발하여 대각선 방향으로 움직이고
사각형 모양을 그리며 출발한 카페로 돌아와야 함

디저트 카페 투어 하는 도중 해당 지역 벗어나면 안됨
카페 투어 중 같은 숫자의 디저트를 팔고 있는 카페 존재해선 안됨
하나의 카페에서 디저트 먹는 것도 안됨
같이 왔던 길을 다시 돌아가는 것도 안됨
되도록 많이 먹는 경로를 찾고 그 때의 디저트 수를 정답으로 출력
만약 디저트 못먹는 경우 -1 출력
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

di = [1, 1, -1, -1]     # 대각선 델타(정사각형 만드는 변 순서대로)
dj = [1, -1, -1, 1]


def cafe_tour(s1, s2, r1, r2, cnt, k):
    global result
    
    if k > 3:               # 정사각형이 되야하므로 방향은 무조건 3번 바뀜
        return
    
    x = s1 + di[k]
    y = s2 + dj[k]
    
    if x < 0 or x >= N or y < 0 or y >= N:      # x, y가 배열 좌표 안에 있어야함
        return
    
    if cnt > 3 and x == r1 and y == r2:     # 정사각형 만들기 위한 최소 cnt는 4, 그리고 다시 처음 좌표로 돌아온다면 최댓값 비교
        if result < cnt:
            result = cnt
            return

    if cafe[x][y] in ate:       # ate 안에 이미 존재하는 디저트라면(이미 먹은 디저트라면) 함수 종료
        return
    
    ate.append(cafe[x][y])      # 먹을 수 있는 디저트이므로 ate에 추가
    cafe_tour(x, y, r1, r2, cnt + 1, k)         # 직진 해보기
    cafe_tour(x, y, r1, r2, cnt + 1, k + 1)     # 다음 방향 가보기
    ate.pop()       # ate에서 pop해주어야 함. 다음 좌표를 확인한것이기 때문에!
    

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    
    result = -1
    
    for i in range(N-2):
        for j in range(1, N-1):
            ate = []                # 새좌표 탐색할때마다 ate 초기화
            ate.append(cafe[i][j])      # 첫 좌표 디저트 ate에 대입
            
            cafe_tour(i, j, i, j, 1, 0)
    
    print(f'#{tc} {result}')
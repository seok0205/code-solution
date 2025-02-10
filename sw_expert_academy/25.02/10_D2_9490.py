"""
D2 9490 풍선팡

M x M 배열에 풍선이 있음. 풍선을 터트리면 상하좌우 풍선이 터지고 들어있는 꽃가루가 날림
종이 꽃가루 개수 A가 주어지면 한 개 풍선 선택 시 날릴 수 있는 꽃가루 합 중 최댓값을 구하는 문제
단 풍선 터트리면 중앙 풍선의 꽃가루 개수만큼 상하좌우 풍선이 추가로 터짐. 만약 2가 들어있다면 상하좌우 2칸반경까지 풍선이 터짐

입력:
T : 테스트 케이스 개수
N, M : 풍선 M개가 N개의 줄에 붙어있음
꽃가루의 개수가 담긴 배열

출력:
'#번호 최대값'
"""

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for i in range(N):
        for j in range(M):
            num_sum = 0
            num_sum += matrix[i][j]
            for m in range(1, matrix[i][j]+1):  # [i][j]의 수만큼 뻗어나가야함 따라서 수에 변화에 따라 반복 횟수 변화
                for k in range(4):  # 상하좌우 더함
                    a = i + di[k] * m
                    b = j + dj[k] * m
                    if 0 <= a <= N-1 and 0 <= b <= M-1: # 단 움직였을 때 배열 안에 있어야함
                        num_sum += matrix[a][b]
            if result < num_sum:    # 최댓값 교체 조건
                result = num_sum
    print(f'#{tc} {result}')
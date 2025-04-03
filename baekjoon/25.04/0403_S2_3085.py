'''
S2 3085 사탕 게임

NxN 크기에 사탕을 채워 놓음. 사탕의 색은 모두 같지 않을 수 있음.
사탕의 색이 다른 인접한 두 칸을 고름. 그 다음 고른 칸에 들어있는 사탕을 서로 교환.
이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 or 열)을 고른 다음 그 사탕을 모두 먹음

사탕이 채워진 상태가 주어졌을 때, 먹을 수 있는 사탕의 최대 개수를 구하는 문제
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def search():           # 가장 큰 사탕 길이 찾기
    global result
    
    if result == N:     # 결과값이 이미 배열 가로나 세로길이와 같다면 함수 종료
        return
    
    for a in range(N):
        num = 1
        for b in range(N-1):            # 가로 배열 길이 찾기
            if candy[a][b] == candy[a][b+1]:
                num += 1
            else:
                num = 1
            result = max(num, result)               # 꾸준히 최댓값 비교
        
        num2 = 1
        for c in range(N-1):            # 세로 배열 길이 찾기
            if candy[c][a] == candy[c+1][a]:
                num2 += 1
            else:
                num2 = 1
            result = max(result, num2)
    

N = int(input())
candy = [list(input()) for _ in range(N)]
result = 0

di = [0, 1]
dj = [1, 0]

for i in range(N):
    for j in range(N):
        target = (i, j)
        for k in range(2):          # 사탕을 인접한 사탕과 바꾸기
            x = target[0] + di[k]
            y = target[1] + dj[k]
            
            if x < 0 or x >= N or y < 0 or y >= N:      # 범위 이탈
                continue
            
            if candy[target[0]][target[1]] == candy[x][y]:      # 서로 같은 사탕이면 안바꿈
                continue
            
            candy[x][y], candy[target[0]][target[1]] = candy[target[0]][target[1]], candy[x][y]
            
            search()        # 바꾸고, 긴 길이 찾고, 다시 바꿔서 제자리로 돌려놓기
            
            candy[x][y], candy[target[0]][target[1]] = candy[target[0]][target[1]], candy[x][y]
            
print(result)
'''
D4 2819 격자판의 숫자 이어 붙이기

4x4 크기 격자판이 있음. 각 격자칸에는 0부터 9사이 숫자가 적혀있음
임의의 위치에서 시작해 동서남북 네 방향으로 인접한 격자로 총 여섯 번 이동하면서,
각 칸에 적힌 숫자를 차례대로 이어 붙이면 7자리의 수가 됨

이동을 할 때에는 한 번 거쳤던 격자칸을 다시 거쳐도 되며, 0으로 시작하는 0102001과 같은 수를 만들 수 있음
격자판을 벗어나는 이동은 불가능
격자판이 주어졌을 때, 만들 수 있는 서로 다른 일곱 자리 수들의 개수를 구하는 문제
'''

import sys
sys.stdin = open('tc.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    matrix = [list(map(int, input().split())) for _ in range(4)]
    
    records = []
    
    for a in range(4):
        for b in range(4):
            target = (a, b)
            visit = [[0] * 4 for _ in range(4)]
            stack = []
            stack.append(target)
            visit[target[0]][target[1]] = 1
            
            di = [0, 0, 1, -1]
            dj = [1, -1, 0, 0]
            
            while stack:
                for i in range(4):
                    x = target[0] + di[i]
                    y = target[1] + dj[i]
                    if 0 <= x < 4 and 0 <= y < 4 and visit[x][y] < 3:
                        stack.append((x, y))
                        visit[x][y] += 1
                        break
                else:
                    target = stack.pop()
            
            print(visit)
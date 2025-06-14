'''
G3 16235 나무 재테크

NxN 크기 땅 구매. 1x1 칸으로 나누어짐. 각 칸은 (r, c)로 나타냄. r은 가장 위에서부터 떨어진 칸의 개수, c는 왼쪽에서 떨어진 칸 개수.
r, c는 1부터 시작. 모든 땅에는 양분이 5만큼 들어있음.

작은 묘목을 구매해 키운 후 팔아서 수익을 얻으려고 함. M개의 나무 구매해 땅에 심음.
1x1 크기 칸에 여러개의 나무 심을 수도 있음.

아래 과정 반복.
1. 봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이 1 증가. 각각의 나무는 나무가 있는 1x1 크기 칸에 있는 양분만 먹을 수 있음.
만약 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을수 없는 나무는 즉시 죽음.

2. 여름에는 봄에 죽은 나무가 양분으로 변함. 각각 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가. 소수점 아래는 버림.

3. 가을에는 나무가 번식. 번식하는 나무는 나이가 5의배수여야함. 인점한 8개의 칸에 나이가 1인 나무가 생김. 땅을 벗어나는 칸엔 나무가 생기지 않음.

4. 땅을 돌아다니며 양분 추가. 각칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어짐.

K년 후 땅에 살아있는 나무의 개수를 구하는 문제.

입력:
N, M, K : 땅의 변 길이, 심을 나무 개수, 몇년후인지.
N개의 줄에 배열의 값 주어짐.
M개의 줄에 나무의 정보 x, y, z. 나무 위치, z는 나무 나이.
'''

import sys
from collections import defaultdict, deque
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline


def four_seasons():     # 한번 실행하면 1년 지남
    death = defaultdict(int)

    # 봄, 여름
    for i, j in trees.items():
        # 양분 먹는 나무, 죽는 나무 판별
        alive = deque()
        tree_list = deque(sorted(j))
        
        for k in tree_list:
            if k <= real_field[i[0]][i[1]]:
                real_field[i[0]][i[1]] -= k
                alive.append(k + 1)
            else:
                death[i] += (k // 2)
        
        # 여름에 죽은 나무들이 양분으로 변함
        trees[i] = alive
        
    # 죽은 나무 있는 땅에 양분 더해줌
    for i, j in death.items():
        real_field[i[0]][i[1]] += j

    # 가을
    di = [0, 0, 1, -1, 1, -1, 1, -1]
    dj = [1, -1, 0, 0, -1, 1, 1, -1]

    add_tree = defaultdict(deque)

    for location, tree in trees.items():
        for k in range(len(tree)):
            if tree[k] % 5 == 0:        # 나무 나이가 5의 배수면 번식
                for n in range(8):
                    nx = location[0] + di[n]
                    ny = location[1] + dj[n]

                    if nx < 0 or nx >= N or ny < 0 or ny >= N:      # 범위 이탈 방지
                        continue

                    add_tree[(nx, ny)].appendleft(1)        # 새로운 나무. 양분은 나이 적은게 먼저 먹으므로 앞으로 삽입

    for i, j in add_tree.items():       # 새로 운나무를 trees 딕셔너리에 확장
        trees[i].extendleft(j)

    # 겨울(원래 땅에 있던 양분 만큼 더해줌)
    for i in range(N):
        for j in range(N):
            real_field[i][j] += field[i][j]


N, M, K = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(N)]
real_field = [[5] * N for _ in range(N)]        # 처음 필드에는 5의 양분이 존재
trees = defaultdict(deque)

for _ in range(M):                          # 처음 나무 위치한 나무들 나타내는 딕셔너리
    x, y, z = map(int, input().split())
    trees[(x-1, y-1)].append(z)

for _ in range(K):              # K년 동안 진행
    four_seasons()

result = 0

for i in trees.values():        # 마지막 딕셔너리에 담긴 나무들의 개수 구하기
    if i:
        result += len(i)

print(result)
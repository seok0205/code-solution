'''
S5 7568 덩치

사람의 덩치를 키와 몸무게, 이 두 개의 값으로 표현하여 그 등수를 매겨보려고 한다.
어떤 사람의 몸무게가 x kg이고 키가 y cm라면 이 사람의 덩치는 (x, y)로 표시
무조건 x, y가 상대방의 수치보다 커야지 덩치가 크다고 할 수 있음.

N명의 집단에서 각 사람의 덩치 등수는 자신보다 더 "큰 덩치"의 사람의 수로 정해진다
만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1이 된다

비교할 수 없는 사람들은 공동 등수가 되고, 2등이 2명이면 3등은 존재하지 않음.

입력:
첫 줄 - 사람 수 N
이어지는 N개의 줄 - 각 사람의 몸무게, 키를 나타내는 정수

출력:
덩치 등수를 구해서 첫 줄에 모두 출력해야함. 공백 분리 필수.
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

N = int(input())
mans = []
rank = []

for _ in range(1, N+1):
    weight, height = map(int, input().split())
    mans.append([weight, height])

for i in range(N):
    w, h = mans[i]
    cnt = 0
    for j in range(N):
        j_w, j_h = mans[j]
        if j_w > w and j_h > h:
            cnt += 1
    rank.append(cnt + 1)

print(*rank)
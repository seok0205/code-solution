'''
S3 2075 N번째 큰 수

문제 설명:
NxN 표에 N**2개가 채워져 있음. 채워진 수에는 한가지 특징이 있음.
모든 수는 자신의 한 칸 위에 있는 수보다 크다는 것.

N번째 큰 수를 찾는 프로그램 작성. 표에 채워진 수는 모두 다름.

입력:
첫째 줄 - N(1 <= N <= 1500)
다음 N개의 줄 - 각 줄마다 N개의 수.
표에 적힌 수는 -10억보다 크거나 같고, 10억보다 작거나 같은 정수.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N = int(input())

'''
python3에서는 메모리 초과. 1500x1500은 제한 12MB넘기 힘듦
'''
# board = [list(map(int, input().split())) for _ in range(N)]

# now_nums = [[board[N-1][i], N-1] for i in range(N)]

# max_cnt = 1
# max_num = -float('inf')
# max_idx = 0

# for i in range(N):
#     if board[N-1][i] > max_num:
#         max_num = board[N-1][i]
#         max_idx = i

# while True:
#     if max_cnt == N:
#         break

#     if now_nums[max_idx][1] - 1 >= 0:
#         now_nums[max_idx][1] -= 1
#         now_nums[max_idx][0] = board[now_nums[max_idx][1]][max_idx]
#     else:
#         now_nums[max_idx][0] = -float('inf')

#     max_cnt += 1
#     max_num = -float('inf')
#     max_idx = 0

#     for i in range(N):
#         if now_nums[i][0] > max_num:
#             max_num = now_nums[i][0]
#             max_idx = i

# print(max_num)

'''
우선순위 큐
'''

import heapq
hq = []

for _ in range(N):
    datas = map(int, input().split())
    for data in datas:
        if len(hq) < N:
            heapq.heappush(hq, data)
        else:
            if hq[0] < data:
                heapq.heappushpop(hq, data)

print(hq[0])
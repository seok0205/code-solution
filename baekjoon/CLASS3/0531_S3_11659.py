'''
S3 11659 구간 합 구하기 4

수 N 개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성

첫 줄에 수의 개수 N과 합을 구해야하는 횟수 M.
둘째 줄에 N개의 수(1000보다 작거나 같은 수)
셋째 줄에 M개의 줄에 합을 구해야 하는 구간 i, j
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

N, M = map(int, input().split())
num_list = list(map(int, input().split()))

sum_list = [0]      # 구간 합의 리스트를 미리 작성
sub = 0

for i in range(len(num_list)):
    sub += num_list[i]
    sum_list.append(sub) 

for i in range(M):
    a, b = map(int, input().split())

    print(sum_list[b] - sum_list[a-1])      # 처음부터 누적합의 리스트를 작성해놓으면 목표 인덱스의 값에서 시작한 인덱스의 합을 빼면 그 구간의 누적 합이다.

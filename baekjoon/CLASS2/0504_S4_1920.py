'''
S4 1920 수 찾기

N개의 정수 A1... An이 주어져있을때, 이 안에 X라는 정수가 존재하는지 알아내는 문제.
M 개의 줄에 답을 출력. 존재하면 1, 아니면 0 출력.

입력:
첫줄 N.
한 줄에 N개의 정수 주어진뒤,
M이 주어짐.
한줄에 M개의 정수가 주어짐(존재하는지 알아내려는 수)
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

N = int(input())

num_list = set(list(map(int, input().split())))     # set로 중복된 수 제거

M = int(input())

nums = list(map(int, input().split()))

for i in nums:          # 찾아야할 수들 순회
    if i in num_list:       # 만약 주어진 수가 있다면, 1 출력
        print(1)
    else:                   # 없으면 0 출력
        print(0)
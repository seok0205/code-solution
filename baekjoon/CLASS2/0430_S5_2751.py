'''
S5 2751 수 정렬하기 2

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램 작성하시오
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

N = int(input())

num_list = list()

for _ in range(N):      # 입력값 리스트에 넣기
    a = int(input())
    num_list.append(a)

num_list.sort()     # 오름차순으로 정렬

for i in num_list:      # 차례로 출력
    print(i)
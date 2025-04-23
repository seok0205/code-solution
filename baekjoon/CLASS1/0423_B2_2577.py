'''
B2 2577 숫자의 개수

세 개의 자연수 A,B,C가 주어질 때 AxBxC를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번 씩 쓰여있는지 구하는 문제

입력:
A
B
C
A,B,C는 모두 100보다 크거나 같고 1000보다 작은 자연수.
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

A = int(input())
B = int(input())
C = int(input())

num = A * B * C
visit = [0] * 10        # 0부터 9까지 출현한 횟수 담을 리스트

for i in str(num):      # 나온 숫자에 해당되는 인덱스 값 증가
    visit[int(i)] += 1

for i in visit:     # 0부터 9까지 나온 횟수 출력
    print(i)
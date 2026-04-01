'''
S3 13305 주유소

문제 설명:
어떤 나라에 N개 도시가 있음. 이 도시들은 일직선 도로 위에 있음.
제일 왼쪽 도시에서 오른쪽 도시로 이동하려고 함.
인접한 두도시 사이 도로들은 서로 길이가 다를 수 있음.
출발할때 기름넣어야 함. 기름통 크기는 무제한.
도로 이동 시 1키로마다 1리터의 기름 사용. 각 도시에는 단 하나의 주유소 있음.
리터당 가격이 다름.

각 도시의 주유소 기름 가격, 연결 도로의 길이를 입력 받을 때, 제일 왼쪽 도시에서 제일 오른쪽 도시로 이동하는 최소 비용을 계산하는 문제.

입력:
첫 줄 - 도시의 개수 N(2 <= N <= 100,000)
두번째 줄 - 왼쪽도로부터 N-1개의 자연수로 주어짐.
세번째 줄 - 주유소 리터당 가격이 N개 왼쪽 도시부터 주어짐.
제일 왼쪽 도시부터 제일 오른쪽 도시까지 거리는 1이상 1,000,000,000이하 자연수.
리터당 가격은 1이상 1,000,000,000이하 자연수.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N = int(input())
roads = list(map(int, input().split()))
gas = list(map(int, input().split()))

last_idx = 0
result = 0

for i in range(N-1):
    if gas[i] < gas[last_idx]:
        last_idx = i
    
    result += (gas[last_idx] * roads[i])

print(result)
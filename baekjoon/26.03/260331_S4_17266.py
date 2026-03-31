'''
S4 17266 어두운 굴다리

문제 설명:
어두운 굴다리가 있고, 길이 어두우면 안감.
굴다리로 가면 최단거리로 집갈수 있는데, 어두워서 빙빙 돌아서 감.
그래서 굴다리 모든 길 0~N에 가로등을 설치할거임.
가로등 설치할 개수 M과 가로등 위치 x가 있음.
높이만 큼 주위를 비출 수 있는 가로등임.
가로등의 높이가 높을 수록 가격이 비싸서, 최소한의 높이로 모든 길 0~N을 밝히려고 함.
최소한의 예산이들 높이를 구하는 문제.
단, 가로등은 모두 높이가 같아야 하고, 정수임.

입력:
첫 줄 - 굴다리 길이 N (1 <= N <= 100000)
두번째 줄 - 가로등 개수 M (1 <= M <= N)
세번째 줄 - M개의 설치할 수 있는 가로등 위치 x (0 <= x <= N)
가로등 위치 x는 오름차순으로 입력받음. 위치 중복 없고 정수.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N = int(input())
M = int(input())
locations = list(map(int, input().split()))

left = 1
right = N
result = N


def check(height, n, locations):
    if locations[0] - height > 0:
        return False
    
    last = locations[0] + height

    for i in range(1, len(locations)):
        s = locations[i] - height

        if last < s:
            return False
        
        last = locations[i] + height

    return last >= n


while left <= right:
    mid = (left + right) // 2

    if check(mid, N, locations):
        result = mid
        right = mid - 1
    else:
        left = mid + 1

print(result)
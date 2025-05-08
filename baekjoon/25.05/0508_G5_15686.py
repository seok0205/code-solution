'''
G5 15686 치킨 배달

NxN 크기 도시 존재. 각 칸은 빈칸, 치킨집, 집 중 하나.
칸은 r행 C열 혹은 위에서부터 r번째 칸, 왼쪽에서부터 c번째 칸을 의미 r, c는 1부터 시작

치킨 거리는 집을 기준으로 정해짐.(가장 가까운 치킨집 사이의 거리) 각각의 집은 치킨 거리를 가지고 있음.
도시의 치킨 거리는 모든 집의 치킨 거리의 합.

일부 치킨집 폐업 시키려고 함. 치킨 집 중 최대 M개 고르고, 나머지 치킨집 폐업 시켜야함. 어떻게 고르면
도시의 치킨 거리가 가장 작게 될지 구하는 문제

입력:
N, M : 도시의 가로 세로
N개의 줄에 도시 정보주어짐
도시 정보는 0은 빈칸, 1은 집, 2는 치킨집. 집의 개수는 2N넘지않음. 적어도 하나는 존재.
치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같음
'''

import sys
sys.stdin = open('tc.txt', 'r')


def get_chicken_house():
    for i in range(N):
        for j in range(N):
            if city[i][j] == 2:
                chicken_house.append((i, j))


def get_chicken_road(location, cnt, length):
    global result

    if cnt == M:
        result = min(result, length)
        return
    else:
        pass


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
result = float('inf')
chicken_house = list()

get_chicken_house()
get_chicken_road(0, 0)
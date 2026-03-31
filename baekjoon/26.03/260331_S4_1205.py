'''
S4 1205 등수 구하기

문제 설명:
각각 노래마다 랭킹 리스트가 있음. 매번 게임마다 얻는 점수가 비오름차순으로 저장.
이 랭킹 리스트의 등수는 보통 위에서부터 몇 번째 있는 점수인지로 결정.
같은 점수가 있을 때는 그러한 점수의 등수 중에 가장 작은 등수가 된다.

예로, 100, 90, 90, 80일 때 각각 등수는 1, 2, 2, 4등.

랭킹 리스트에 올라 갈 수 있는 점수의 개수가 P로 주어짐. 리스트에 있는 점수 N개가 비오름차순으로 주어지고, 새로운 점수가 주어짐.
이때 새로운 점수가 랭킹 리스트에서 몇 등 하는지 구하는 프로그램 작성.
만약 점수가 랭킹 리스트에 올라갈 수 없을 정도로 낮으면 -1출력.
랭킹 리스트가 꽉 차있을대, 새 점수가 이전 점수보다 더 좋을 때만 점수가 바뀜.

입력:
첫째줄 - N, 새 점수, P 주어짐. (10 <= P <= 50), (0 <= N <= P)
모든 점수는 2,000,000,000보다 작거나 같은 자연수 또는 0.
랭킹 리스트의 점수들은 비오름차순(내림차순). 둘째줄은 N이 0보다 큰 경우만 주어짐.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N, new_score, P = map(int, input().split())

if N > 0:
    rank = list(map(int, input().split()))
    result = 1
    if N >= P:
        rank = rank[:P]
        if rank[-1] >= new_score:
            result = -1

    if result != -1:
        for i in range(N):
            if rank[i] > new_score:
                result += 1
            else:
                break
    print(result)
else:
    print(1)
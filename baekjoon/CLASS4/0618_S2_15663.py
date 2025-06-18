'''
S2 15663 N과 M (9)

N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 문제
1. N개의 자연수 중에서 M개를 고른 수열

입력:
N, M
N개의 수 주어짐. 10000보다 작거나 같은 자연수들.

출력:
중복 수열 여러 번 출력 x. 수열은 사전 순으로 증가하는 순서로 출력
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline


def find_sequence(cnt):     # 수열 찾기
    check_num = 0           # 조합 숫자
    if cnt == M:
        print(' '.join(map(str, num)))      # 길이 충족했을 때 출력
        return
    
    for i in range(N):
        if check_num != num_list[i] and visit[i] == 0:      # 똑같은 숫자 사용하지 않고 있고, 조합에 사용도 안한 숫자면!
            num.append(num_list[i])     # 조합에 사용
            visit[i] = 1                # 조합 사용 하니까 리스트 표시
            check_num = num_list[i]     # 해당 자리 숫자는 사용 중.
            find_sequence(cnt + 1)      # dfs 형식 재귀 호출
            num.pop()                   # 조합에 사용했을 때 모든 경우의 수 확인했으니 조합에서 뺌
            visit[i] = 0                # 방문 리스트 표시 해제


N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()     # 출력 시 사전 순으로 출력해야함.
visit = [0] * N     # 숫자 조합에 사용했는지 여부 확인 리스트
num = []            # 재귀 호출 할때마다 담긴 숫자가 바뀜

find_sequence(0)
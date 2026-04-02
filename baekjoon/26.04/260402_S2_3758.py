'''
S2 3758 KCPC

문제 설명:
총 k개의 문제를 풀게 됨.
어떤 문제 풀이를 서버에 제출하면 문제에 대해 0점에서 100점 사이 점수를 얻음.
풀이 제출 팀의 ID, 문제 번호, 점수가 로그에 제출되는 시간 그대로 저장됨.
한 문제에 대한 풀이를 여러번 제출 가능.
그 중 최고 점수가 그 문제에 대한 최종 점수.
만약 아무 풀이도 제출안했으면 0점.

팀의 점수는 각 문제에 받은 점수의 총합. 순위는 팀보다 높은 점수 받은 팀수 + 1임.
점수 동일 팀도 여럿 있을 수 있음.

1. 최종 점수가 같은 경우, 풀이를 제출한 횟수가 적은 팀의 순위가 높다.
2. 최종 점수도 같고, 횟수도 같으면, 제출 시간 빠른 팀이 높다.

동시에 제출되는 풀이 없고, 모든 팀이 한번은 풀이 제출했다고 가정.
팀의 순위를 구하는 문제.

입력:
T의 테스트 데이터로 구성.
TC 첫 줄에는 팀의 개수 n, 문제 개수 k, 우리팀의 ID, 로그 개수 m개가 주어짐.
(3 <= n, k <= 100, 1 <= t <= n, 3 <= m <= 10,000)
다음 m개의 줄에는 각 풀이에 대한 정보가 제출 순서대로 주어짐.
팀 ID i, 문제 번호 j, 획득 점수 s가 주어짐.
(1 <= i <= n, 1 <= j <= k, 0 <= s <= 100)
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split())
    score = [[0] * (k+1) for _ in range(n+1)]
    rank_info = [[0] * 2 for _ in range(n+1)]

    for num in range(m):
        i, j, s = map(int, input().split())
        
        if score[i][j] < s:
            score[i][j] = s
        
        rank_info[i][1] = num
        rank_info[i][0] += 1

    for num in range(n+1):
        rank_info[num].append(sum(score[num]))

    sub = sorted(rank_info[1:], key=lambda x: (-x[2], x[0], x[1]))
    print(sub.index(rank_info[t]) + 1)
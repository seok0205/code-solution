'''
S3 9017 크로스 컨트리

문제 설명:
크로스 컨트리 코스는 일반적으로 4에서 12키로.
주자들의 개인 성적을 매기고, 팀의 점수를 계산.
한팀은 여섯 명의 선수로 구성. 팀 점수는 상위 네 명의 주자의 점수를 합하여 계산. 점수는 자격을 갖춘 팀의 주자들에게만 주어지며, 결승점 통과 순서대로 점수를 받음.
이 점수에 더하여 가장 낮은 점수를 얻는 팀이 우승하게됨. 여섯명의 주자가 참가하지 못한 팀은 점수 계산에서 제외됨.
동점인 경우 다섯 번째 주자가 가장 빨리 들어온 팀이 우승.

모든 선수들의 등수가 주어질 때, 우승 팀 구하는 문제.
여섯명 보다 많은 선수가 참가하는 팀은 없고, 적어도 한팀은 참가선수가 여섯.
모든 선수는 끝까지 완주한다가 가정.

입력:
T개의 테스트 케이스.
각 테스트 케이스 첫 줄에는 하나의 정수 N(6<=N<=1000).
두번째 줄에 팀 번호를 나타내는 N개의 정수가 공백두고 주어짐.
각 팀은 1과 M(1 <= M <= 200)사이의 정수로 표현

출력:
하나의 TC당 우승팀 번호 하나 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    records = list(map(int, input().split()))
    
    teams = max(records)
    pass_list = [False] * (teams+1)
    for i in range(1, teams+1):
        if records.count(i) == 6:
            pass_list[i] = True
    
    score_list = [[0] * 4 for _ in range(teams+1)]
    score = 1
    for i in range(N):
        if pass_list[records[i]]:
            if score_list[records[i]][1] == 4:
                score_list[records[i]][2] += score
            elif score_list[records[i]][1] == 5:
                score_list[records[i]][3] += score
            else:
                score_list[records[i]][0] += score
            score_list[records[i]][1] += 1
            score += 1
    
    min_score = float('inf')
    result = 0
    for i in range(1, teams+1):
        if pass_list[i] == False:
            continue

        if min_score > score_list[i][0]:
            min_score = score_list[i][0]
            result = i
        else:
            if min_score == score_list[i][0]:
                if score_list[result][2] > score_list[i][2]:
                    result = i

    print(result)
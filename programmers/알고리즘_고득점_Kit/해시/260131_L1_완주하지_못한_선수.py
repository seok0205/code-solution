'''
완주하지 못한 선수

한 명 빼고 모든 선수가 마라톤 완주.
선수 이름 담긴 배열 participant, 완주한 선수 이름 담긴 배열 completion이 주어질 때,
완주하지 못한 선수의 이름을 return.

제약:
참여 선수 1~100,000
completion의 길이는 participant의 길이보다 1 작음.
참가자 이름은 1 ~ 20 개의 알파벳 소문자.
동명이인 있을 수 있음.
'''

def solution(participant, completion):
    goal = {}
    
    for name in participant:
        if name not in goal.keys():
            goal[name] = 1
        else:
            goal[name] += 1
    
    for player in completion:
        goal[player] -= 1
        if goal[player] == 0:
            goal.pop(player)
            
    a = list(goal.keys())
    answer = a[0]
    return answer
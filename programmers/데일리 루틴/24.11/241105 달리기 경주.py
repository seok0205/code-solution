'''
1등부터 꼴등까지 현재 등수를 담은 리스트 players, 순위를 앞 선수와 바꾼 선수들의 이름을 담은 리스트 callings가 주어진다.
경주가 끝났을 때 등수를 담은 리스트를 출력하는 문제.
callings에 있는 선수들만이 순위를 뒤바꾼 선수들이다.
'''

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

def solution(players, callings):
    rank = {player : num for num, player in enumerate(players)} # 선수, 등수를 딕셔너리 형태로 접근.

    for i in callings:  # 순위 뒤바꾼 선수만 시행.
        n = rank[i]
        players[n], players[n-1] = players[n-1], players[n] # 앞에서 뛰는 선수와 순위 변동.
        rank[players[n]], rank[players[n-1]] = n, n-1   # 딕셔너리의 정보도 변동.
    
    return players

print(solution(players, callings))

'''
for문으로 한선수가 순위를 바꿀때마다 리스트의 형태를 바꾸는 풀이도 있지만 시간복잡도가 문제가 된다.
제한 사항이 players 가 50000, callings가 백만의 길이까지 존재하는데, 시간복잡도가 백억까지 치솟는다.
따라서 시간복잡도가 O(1)인 딕셔너리를 활용해서 시간을 절약.
'''
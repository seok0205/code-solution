'''
피로도 시스템이 있음. 0이상의 정수로 표현됨.
탐험을 시작하기 위한 '최소 필요 피로도'가 있고 탐험이 끝났을 때 소모되는 '소모 피로도'가 있음.
하루에 한 번 갈 수 있는 던전이 여러개 주어질 때, 최대한 많이 갈 수 있는 던전 수를 반환하는 문제.

제한 사항 :
1 <= k <= 5000 자연수.
1 <= dungeons의 세로 길이(던전 개수) <= 8
dungeons의 가로 길이는 2. [최.필.피, 소.피].
최필피와 소피는 1이상 1000이하 자연수.
서로 다른 던전의 피로도 구성이 같을 수 있음.

접근 :
1. 모든 순열의 결과를 구하고 하나씩 탐색.
2. 모든 던전 순열의 조합을 일일이 탐색 후, 최대 던전 개수 측정.
'''

from itertools import permutations  # 순열

k = 80
dungeons = [[80,20],[50,40],[30,10]]

result = [] # 하루 탐험한 던전 개수 경우의 수 저장.
dg_list = list(permutations(dungeons)) # 튜플의 형태로 리스트 안에 나열.
for i in dg_list:   # i는 튜플로 이루어진 순열 중 하나.
    cnt = 0 # 하루 탐험한 던전 개수
    k_1 = k # 처음 피로도
    for m, n in i:  # m은 최필피, n은 소피.
        if m > k_1: # 최소 필요 피로도가 만족 못할 시 던전 입장 못함.
            break   # 중지.
        else:   # 만족 한다면,
            k_1 = k_1 - n   # 피로도 소모.
            cnt += 1    # 던전 입장 횟수 1 증가.
    
    result.append(cnt)  # for문에서 쌓은 cnt를 result에 추가

print(max(result))  # result에 쌓인 cnt 값중 max값이 최대 입장 던전 개수임.

'''
다른 풀어 : 백트래킹
max_count = 0

def dfs(k, count, dungeons, visited):
    global max_count 
    if count > max_count: # 현재 탐험 던전 수가 이전 max_count보다 많으면 max_count 갱신
        max_count = count
    
    for i in range(len(dungeons)):  #모든 던전 순회, 탐험하지 않았고, 체력이 최필피보다 크거나 같으면 탐험 가능.
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True   # 방문 업데이트.
            dfs(k - dungeons[i][1], count + 1, dungeons, visited)   # 체력 소모 후, 재귀 호출
            visited[i] = False  # 백트래킹 위해 방문 기록 초기화.
        
def solution(k, dungeons):
    global max_count
    visited = [False] * len(dungeons)   # visited 리스트 초기화.
    dfs(k, 0, dungeons, visited)    # dfs 호출.
    return max_count    # max_count 반환.
'''
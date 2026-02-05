'''`
L2 피로도

문제 설명:
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
복습 문제. 1년전에는 순열로 풀었는데, 완탐 관련 문제 풀다보니 dfs 형식으로 푸는게 더 편해서 dfs 도입.
'''

answer = 0

def dfs(k, dungeons, visit, cnt):
    global answer
    answer = max(answer, cnt)
    
    for i in range(len(dungeons)):
        if not visit[i] and k >= dungeons[i][0]:
            visit[i] = 1
            dfs(k-dungeons[i][1], dungeons, visit, cnt+1)
            visit[i] = 0

def solution(k, dungeons):
    visit = [0] * len(dungeons)
    dfs(k, dungeons, visit, 0)
    return answer
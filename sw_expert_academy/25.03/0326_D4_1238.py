'''
D4 1238 Contact

비상연락망과 연락을 시작하는 당번에 대한 정보가 주어질 때, 가장 나중에
연락을 받게 되는 사람 중 번호가 가장 큰 사람을 구하는 함수를 작성

서로에게 한번에 연락은 불가능
한 명이 다수에게 전화 가능할시 동시에 전달
연락 퍼지는 속도는 일정
한 번 연락 받은 사람에게 다시 연락하는 일 없음
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

from collections import deque


def bfs(s):             # bfs 활용
    q = deque()
    q.append(s)
    visit[s] = 1
    
    while q:
        target = q.popleft()            # 디큐
        for k in network[target]:       # 전화할수있는사람들에게 전화
            if not visit[k]:            # 전화안했던 사람들에게만
                visit[k] = visit[target] + 1        # 전화거는 사람이 받았떤 순번의 +1, 어차피 연결된 사람들은 동시에 전화받음
                q.append(k)             # 다음 이사람들도 전화를 걸어야하므로 인큐


for tc in range(1, 11):
    D, S = map(int, input().split())
    network = [[] for _ in range(101)]
    info = list(map(int, input().split()))
    
    for i in range(D//2):           # 간선 정보 저장해줌
        a = info[i*2]
        b = info[i*2+1]
        if b not in network[a]:     # 중복 정보도 있다고 했으니 중복된건 제외하고 추가
            network[a].append(b)
            
    visit = [0] * 101       # 최대 100명의 인원 존재
    bfs(S)
    
    result = S
    for i in range(101):
        if visit[i] == max(visit):      # 최댓값 같으면 설정해줌. 번호 큰사람 출력이므로 결국 가장 번호 큰사람이 설정됨
            result = i
            
    print(f'#{tc} {result}')
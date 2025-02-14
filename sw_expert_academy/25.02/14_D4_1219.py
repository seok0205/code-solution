'''
D4 1219 길찾기

A에서 B까지 가는 경로가 존재하는지 조사
A, B는 0, 99 고정
모든 길은 순서쌍으로 나타남
가는 경로 개수 상관없이 한가지 길이라도 존재하면 경로가 존재하는 것
다시 거슬러 이전으로 돌아갈 수 없음
'''


def dfs_road(s, v):     # dfs 함수
    visited = [0] * (v + 1)
    stack = []
    
    while True:                     # 모든 노드를 검사해서 시작점부터
        if visited[s] == 0:         # 목표지점까지 들릴 수 있는 노드들은 1로 표현
            visited[s] = 1
        for w in way[s]:
            if visited[w] == 0:
                stack.append(s)
                s = w
                break
        else:
            if stack:
                s = stack.pop()
            else:
                break
    return visited


T = 10

for tc in range(1, T+1):
    tc_num, road_num = map(int, input().split())
    way = [[] for _ in range(100)]
    
    lst = list(map(int, input().split()))
    for i in range(road_num):
        a = lst[i*2]
        b = lst[i*2+1]
        
        way[a].append(b)
    
    result = dfs_road(0, 99)
    if result[0] and result[-1]:        # 만약 처음과 끝이 둘다 1이면 경로 존재
        print(f'#{tc} 1')
    else:                               # 존재하지 않으면 0(끝점만 1인지 확인하면 됨)
        print(f'#{tc} 0')
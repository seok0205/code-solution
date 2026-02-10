'''
L3 섬 연결하기

문제 설명:
n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.

다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다. 예를 들어 A 섬과 B 섬 사이에 다리가 있고, B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.

제약:
섬의 개수 n은 1 이상 100 이하입니다.
costs의 길이는 ((n-1) * n) / 2이하입니다.
임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고, costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.
같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다. 즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.
모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.
연결할 수 없는 섬은 주어지지 않습니다.
'''

# 크루스칼 풀이
def kruscal_solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]
    
    def find(parent, i):
        if parent[i] == i:
            return i
        parent[i] = find(parent, parent[i])
        return parent[i]

    def union(parent, a, b):
        root_a = find(parent, a)
        root_b = find(parent, b)
        
        if root_a < root_b:
            parent[root_b] = root_a
        else:
            parent[root_a] = root_b
        
    cnt = 0
    
    for s, e, cost in costs:
        if find(parent, s) != find(parent, e):
            union(parent, s, e)
            answer += cost
            cnt += 1
            
            if cnt == n - 1:
                break
                
    return answer


# 프림 풀이
import heapq

def prim_solution(n, costs):
    answer = 0
    edge = [[] for _ in range(n)]

    for s, e, cost in costs:
        edge[s].append((cost, e))
        edge[e].append((cost, s))

    q = [(0, 0)]
    visit = [0] * n
    cnt = 0

    while q:
        cost, x = heapq.heappop(q)

        if visit[x]:
            continue

        visit[x] = 1
        answer += cost

        if cnt == n-1:
            break

        for n_cost, nx in edge[x]:
            if not visit[nx]:
                heapq.heappush(q, (n_cost, nx))
    return answer
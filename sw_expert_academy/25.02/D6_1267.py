import sys
sys.stdin = open('tc.txt', 'r')

T = 1

for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge = list(map(int, input().split()))
    edge_lst = [[] for _ in range(V+1)]
    preceding_lst = [[] for _ in range(V+1)]
    for i in range(E):
        a = edge[i*2]
        b = edge[i*2+1]
        
        edge_lst[a].append(b)
        preceding_lst[b].append(a)

    print(edge_lst)
    print(preceding_lst)
    
    def findWay(s, e=V):
        visited = [0] * (e+1)
        stack = []
        
        while True:
            stack.append(s)
            if len(preceding_lst[s]) == 0 and visited[s] == 0:
                visited[s] = 1
                
            for w in edge_lst[s]:
                if len(preceding_lst[w]) == 0 and visited[w] == 0:
                    s = w
                    break
            else:
                if stack:
                    s = stack.pop()
                else:
                    break
    
    start = 0
    
    for i in range(1, len(preceding_lst)):
        if len(preceding_lst[i]) == 0:
            start = i
            break
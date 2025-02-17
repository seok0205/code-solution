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
    
    visited = [0] * (V+1)

    def findStart(lst):
        for i in range(1, len(lst)):
            if len(lst[i]) == 0:
                start = i
                break
        return start
    
    def findWay(s, e=V, visited=visited):
        result = []
        stack = []
        stack.append(s)
        
        while True:
            if len(preceding_lst[s]) == 0 and visited[s] == 0:
                visited[s] = 1
                result.append(s)
                
            for w in edge_lst[s]:
                if len(preceding_lst[w]) == 0 and visited[w] == 0:
                    stack.append(w)
                    s = w
                    break
            else:
                if stack:
                    s = stack.pop()
                else:
                    break

        return result
    
    print(findWay(4))
'''
L5 방의 개수

문제 설명:
원점(0,0)에서 시작해서 아래처럼 숫자가 적힌 방향으로 이동하며 선을 긋습니다.
그림을 그릴 때, 사방이 막히면 방하나로 샙니다.
이동하는 방향이 담긴 배열 arrows가 매개변수로 주어질 때, 방의 갯수를 return 하도록 solution 함수를 작성하세요.

제약:
- 배열 arrows의 크기는 1 이상 100,000 이하 입니다.
- arrows의 원소는 0 이상 7 이하 입니다.
- 방은 다른 방으로 둘러 싸여질 수 있습니다.
'''

def solution(arrows):
    answer = 0
    xi = [-1, -1, 0, 1, 1, 1, 0, -1]
    yi = [0, 1, 1, 1, 0, -1, -1, -1]
    
    visit_node = set()
    visit_edge = set()
    
    now = (0, 0)
    visit_node.add(now)
    
    for arrow in arrows:
        for _ in range(2):
            nx = now[0] + xi[arrow]
            ny = now[1] + yi[arrow]
            
            next_node = (nx, ny)
            
            if next_node in visit_node and (now, next_node) not in visit_edge:
                answer += 1
            
            visit_node.add(next_node)
            visit_edge.add((now, next_node))
            visit_edge.add((next_node, now))
            
            now = next_node
    return answer
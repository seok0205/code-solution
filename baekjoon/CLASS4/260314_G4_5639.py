'''
G4 5639 이진 검색 트리

문제 설명:
이진 검색 트리는 조건 세가지를 만족하는 이진 트리임.
1. 노드의 왼쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 작음.
2. 노드의 오른쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 큼.
3. 왼쪽, 오른쪽 서브트리도 이진 검색트리임.

전위 순회 (루트-왼쪽-오른쪽)은 루트를 방문하고, 왼쪽 서브트리, 오른쪽 서브 트리를 순서대로 방문하면서 노드의 키를 출력한다.
후위 순회 (왼쪽-오른쪽-루트)는 왼쪽 서브트리, 오른쪽 서브트리, 루트 노드 순서대로 키를 출력한다.
이진 검색 트리를 전위 순회한 결과가 주어질 때, 이 트리를 후위 순회한 결과를 구하는 프로그램을 작성.
'''

import sys
sys.setrecursionlimit(10**4)
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.read
output = sys.stdout.write

tree = list(map(int, input().split()))


def post(s, e):
    if s > e:
        return
    
    root = tree[s]
    m = e + 1

    l = s + 1
    r = e

    while l <= r:
        t = (l + r) // 2
        if tree[t] > root:
            m = t
            r = t - 1
        else:
            l = t + 1
    
    post(s+1, m-1)
    post(m, e)
    output(str(root) + '\n')

post(0, len(tree)-1)
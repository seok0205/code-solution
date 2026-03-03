'''
S1 1991 트리 순회

문제 설명:
이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.

전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)

입력:
첫째 줄 N(1 <= 26)
둘째 줄 N개의 줄에 걸쳐 각 노드와 왼쪽자식노드, 오른쪽자식노드
노드의 이름은 A부터 알파벳 대문자. 항상 A가 루트 노드. 자식 노드 없으면 . 표현
'''

import sys

# sys.stdin = open('tc.txt')
input = sys.stdin.readline
output = sys.stdout.write

N = int(input())
tree_dic = dict()

for _ in range(N):
    parents, left, right = input().split()
    tree_dic[parents] = (left, right)


def preorder(node):
    if node == '.':
        return
    
    output(node)
    preorder(tree_dic[node][0])
    preorder(tree_dic[node][1])


def inorder(node):
    if node == '.':
        return
    
    inorder(tree_dic[node][0])
    output(node)
    inorder(tree_dic[node][1])


def postorder(node):
    if node == '.':
        return
    
    postorder(tree_dic[node][0])
    postorder(tree_dic[node][1])
    output(node)


root = 'A'
preorder(root)
output('\n')
inorder(root)
output('\n')
postorder(root)
'''
S4 4949 균형잡힌 세상

문제 설명:
문자열 주어질 때 균형이 맞는 지 판단하는 프로그램 작성

소괄호, 대괄호 2종류

1. 왼쪽 소괄호는 오른쪽 소괄호와만 짝
2. 왼쪽 대괄호는 오른쪽 대괄호와만 짝
3. 모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호 존재
4. 모든 괄호 짝은 1대1 매칭 가능. 둘 이상 안됨
5. 짝이루는 두 괄호가 있을 때, 그 사이 문자열도 균형 잡혀야 함.

입력:
길이는 100글자(일반 영어단어도 출현). 마지막에 온점이 종료 조건

출력:
균형 잡히면 yes, 아니면 no 출력
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

result = []

while True:
    world = input()
    if world == '.':
        break

    stack = []

    for i in world:
        if i == '(':
            stack.append('(')
        elif i == '[':
            stack.append('[')
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')

    if stack:
        result.append('no')
    else:
        result.append('yes')

for i in result:
    print(i)
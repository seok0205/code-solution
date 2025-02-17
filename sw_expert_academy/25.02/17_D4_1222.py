'''
D4 1222 계산기 1

문자열로 이루어진 계산식이 주어질 때, 후위 표기식으로 바꾸어 계산하는 프로그램 작성
문자열 계산식을 구성하는 연산자는 '+' 하나, 피연산자인 숫자는 0~9의 정수.
'''

import sys
sys.stdin = open('tc.txt', 'r')


def postFix(string):        # 후위 표기식 바꾸는 함수
    result = ''
    stack = list()          # 후위 표기식으로 표현하려면 스택에 연산자를 저장
    
    for i in string:
        if i == '+':        # + 연산자가 나오면 스택에 추가
            stack.append(i)
        else:               # 숫자가 나오면 식에 추가.
            result += i
            if stack:       # 만약 스택에 연산자가 있다면,(+만 나오기때문에 우선순위가 없음 따라서 2개의 숫자가 나오면 연산자가 바로 별도의 조건없이 꺼내져야함)
                result += stack.pop()
    
    return result


def calculate(string):      # 후위 표기식을 받아 계산하는 함수
    stack = list()          # 계산에선 숫자를 스택에 저장
    
    for i in string:
        if i == '+':        # + 연산자가 나오면 앞서 저장된 두개의 숫자를 꺼내 계산 후 스택에 다시 추가
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        else:
            stack.append(int(i))    # 숫자가 나오면 스택에 추가
    
    return stack[-1]


T = 10

for tc in range(1, T+1):
    length = int(input())
    expression = input()
    
    pf = postFix(expression)
    calculated_result = calculate(pf)
    
    print(f'#{tc} {calculated_result}')
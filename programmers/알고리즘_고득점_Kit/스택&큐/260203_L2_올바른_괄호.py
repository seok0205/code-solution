'''
L2 올바른 괄호

문제 설명:
괄호가 바르게 짝지어졌다는 것은 '('로 열렸으면 반드시 짝지어서 ')'로 닫혀야 한단 뜻.

- "()()" 혹은 "(())()"는 올바른 괄호.
- ")()(" 혹은 "(()("는 올바르지 않은 괄호.

'(',')'로만 이루어진 문자열 s가 주어질 때, 문자열 s가 올바른 괄호면 true 반환, 올바르지 않은 괄호면 false 반환하는 함수 작성.

제약:
문자열 s 길이: 100,000 이하의 자연수
문자열 s는 '(' 혹은 ')'로만 이루어짐.
'''

def solution(s):
    stack = []
    
    for i in s:
        if i == '(':
            stack.append(i)
        elif stack and i == ')':
            stack.pop()
        else:
            return False
    
    if stack:
        return False
    else:
        return True
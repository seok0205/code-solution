'''
D2 16476 괄호검사

주어진 입력에서 {}, ()가 제대로 짝을 이뤘는지 확인하는 문제
{()}는 정상, {(})는 비정상
정상적 짝이면 1, 아니면 0 출력
'''

T = int(input())

for tc in range(1, T+1):
    string = list(input())

    top = -1        # stack의 top(맨위의, 현재 스택에서 꺼내면 먼저 나오는 것)
    stack = list()      # 스택 생성

    result = 1      # 기본 값 1(혹은 0)

    for i in string:
        if i == '(' or i == '{':        # 문자열에서 시작인 '(' 혹은 '{'이 출현하면 스택에 추가
            top += 1        # 현재 top이 1 증가. 스택에 값이 생성된다는 뜻. 즉시 꺼내면 이것부터 나옴
            stack.append(i)
        elif stack and i == ')' and stack[top] == '(':      # 스택의 top에 '('이 존재하는데 ')'이 출현하면 스택의 '(' 꺼냄(짝이 맞다는 뜻)
            stack.pop(top)
            top -= 1
        elif stack and i == '}' and stack[top] == '{':      # 스택의 top에 '{'이 존재하는데 '}'이 출현하면 스택의 '{' 꺼냄
            stack.pop(top)
            top -= 1
        elif i == '}' or i == ')':      # 앞에 {, (가 나오지 않았는데 }, )이 출현하면 잘못된 짝이므로 break 후 0출력
            result = 0
            break
    else:       # for문을 break없이 실행했을 때, 스택에 값이 있으면 0, 없으면 1
        if stack:
            result = 0
        else:
            result = 1

    print(f'#{tc} {result}')

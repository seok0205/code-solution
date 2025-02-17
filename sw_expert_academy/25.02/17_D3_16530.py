'''
D3 16530 Forth

Forth는 스택 연산 기반이어서 후위 표기법 사용. 주어진 연산식을 출력하는 문제.
연산 불가능한 경우(잘못된 형식) 'error' 출력
'''

T = int(input())

for tc in range(1, T+1):
    calculation = list(map(str, input().split()))

    result = 0
    stack = []
    for i in calculation:   # 식의 요소들을 하나씩 탐색
        if i in '*/+-':     # i가 연산자라면
            if len(stack) == 1 or len(stack) == 0:  # 만약 스택에 수가 하나만 있거나 없을때,
                print(f'#{tc} error')               # 연산을 하지 못함. error 출력
                break
            elif len(stack) > 1:        # 스택에 수가 두개 이상 있으면
                b = stack.pop()         # 하나씩 꺼냄
                a = stack.pop()
                if i == '+':            # 연산자의 형태에 따라 사칙연산 후 결과 숫자를 스택에 다시 숫자를 넣음
                    num = a + b
                    stack.append(num)
                elif i == '-':
                    num = a - b
                    stack.append(num)
                elif i == '*':
                    num = a * b
                    stack.append(num)
                elif i == '/':
                    num = a // b
                    stack.append(num)
        elif i == '.':                  # 만약 .이 등장하면
            result = stack.pop()        # 마지막 계산한 결과 출력
            if stack:                   # 그런데 마지막 계산한 결과를 꺼냈는데 스택에 연산이 안된 숫자가 남아있으면. 연산 불가능이므로 에러 출력.
                print(f'#{tc} error')
                break
            print(f'#{tc} {result}')
            break
        else:                           # 연산자나 온점이 아니면 숫자란 뜻이므로 스택에 추가.
            stack.append(int(i))

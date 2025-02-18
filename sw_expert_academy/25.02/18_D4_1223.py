'''
D4 1223 계산기 2

문자열형태 계산식이 주어질때, 계산식을 후위 표기식으로 바꾸어 계산.
'''


def make_postfix(string):
    fir = {'+': 1, '-': 1, '*': 2, '/': 2}  # 식에서의 우선순위 설정 +-는 */보다 우선순위에서 밀림
    
    stack = []
    result = ''
    
    for i in string:        # 식에서 문자를 하나씩 보면서
        if i in "+-/*":     # 연산자면
            while stack and fir[stack[-1]] >= fir[i]:       # 스택에 연산자가 존재하는데, 스택의 연산자가 현재 연산자보다 우선순위가 크거나 같으면,
                result += stack.pop()                       # 꺼내서 후위표기식에 추가
            stack.append(i)     # 스택에 추가
        else:               # 숫자면
            result += i     # 식에 추가
        
    while stack:            # 마지막 스택에 남은 연산자는 제대로된 식이면 하나가 무조건 남음 위 if 문에서 꺼내서 추가한뒤 마지막에 해당되는 연산자는 추가되고 pop이 안되기 때문
        result += stack.pop()    # 따라서 꺼내서 식에 마지막으로 추가

    return result

def calculate_postfix(string):
    stack = []
    
    for i in string:
        if i in '+-/*':         # 연산자면 스택의 숫자를 2개 빼서
            b = stack.pop()
            a = stack.pop()
            
            if i == '+':        # 해당되는 연산을 한 후에
                v = a + b
            elif i == '-':
                v = a - b
            elif i == '*':
                v = a * b
            elif i == '/':
                v = a / b
            
            stack.append(v)     # 스택에 다시 추가
        else:
            stack.append(int(i))    # 숫자는 스택에 추가
    
    return stack[-1]        # 스택의 마지막 값이 연산 완료 값


T = 10

for tc in range(1, T+1):
    N = int(input())
    string = input()
        
    string = make_postfix(string)
    print(f'#{tc} {calculate_postfix(string)}')
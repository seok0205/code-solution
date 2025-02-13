'''
D4 1218 괄호 짝짓기

4종류의 괄호문자들 '()', '[]', '{}', '<>'
문자열에 사용된 괄호들의 짝이 모두 맞는지 판별
'''

T = 10

for tc in range(1, T+1):
    length = int(input())
    string = list(input())

    top = -1
    stack = list()
 
    dic = {'{': '}', '(': ')', '[': ']', '<': '>'}      # key는 처음 나오는 괄호, value는 괄호에 알맞은 끝 괄호
    target = list(dic.keys())       # 처음 찾아야 하는 괄호 리스트
    end_target = list(dic.values())        # 끝 괄호 리스트

    for i in string:        # 문자열을 순회하면서
        if i in target:     # 처음 찾아야할 괄호가 나오면 스택에 추가
            top += 1
            stack.append(i)
        elif stack and i == current_target:     # 스택에 찾아야하는 괄호가 쌓여있고, 현재 타겟과 같으면 제거
            stack.pop(top)
            top -= 1
        elif i in wrong_target_lst:     # 만약 나오지 말아야할 끝괄호가 먼저 나온다면 결과값이 0이 나오고 반복문 탈출(끝 괄호가 먼저나오면 짝이 맞을 수 없음)
            result = 0
            break
        wrong_target_lst = end_target.copy()   # 위 elif문에 들어갈 wrong_target_lst는 스택의 맨 위값에 따라 바뀌어야함. 스택에 아무것도 없다면 4가지 끝 괄호 모두 나와서는 안됨
        if stack:       # 스택에 값이 존재할때,
            current_target = dic[stack[top]]        # 현재 찾아야할 끝 괄호를 딕셔너리에서 찾아 설정
            current_target_index = end_target.index(current_target)        # 끝 괄호의 인덱스를 찾아
            wrong_target_lst.pop(current_target_index)              # wrong_target_lst에서 삭제하고 다음 반복 진입
    else:       # 만약 for문을 정상적으로 break없이 실행했다면
        if stack:       # 스택에 값이 남아있따면 0
            result = 0
        else:           # 그렇지 않다면 1
            result = 1

    print(f'#{tc} {result}')

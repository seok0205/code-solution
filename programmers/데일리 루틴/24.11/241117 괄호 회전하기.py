'''
1. '()', '[]', '{}'는 올바른 괄호 문자열.
2. A가 올바르다면, (A), [A], {A}도 올바름. ex. ([])
3. A, B가 올바르다면, AB도 올바름. ex. {}([])
s가 매개변수로 주어질때, s를 왼쪽으로 x칸만큼 회전시켰을 때 s가 올바르게 되게 하는 x의 개수를 구하라.

제한 사항 :
1. 1 <= len(s) <= 1000

접근 :
1. s의 첫 문자 제거 후 해당 문자를 리스트 끝에 추가.
2. 과정 반복하면서 열린 괄호와 닫힌 괄호끼리의 짝이 맞게 되면 결과값 1씩 증가.
'''

s = "[](){}"

result = 0
n = len(s)
for i in range(n):  # 문자열 회전.
    stack = []
    for j in range(n):  # 반복 1회마다 회전 1회
        c = s[(i + j) % n]  # i는 첫 번째 문자 인덱스 위치. j는 바로 다음에 위치하는 문자.
        if c == "(" or c == "[" or c == "{":    # 여는 괄호 추가.
            stack.append(c)
        else:
            if not stack:   # 닫는 괄호를 참조하는데 스택에 아무 괄호도 없으면 다음 참조값으로 넘어감.
                break
            if c == ")" and stack[-1] == "(":   # c가 참조중인 문자가 닫힌 괄호일 때 스택에 여는 괄호가 있는 경우.
                stack.pop() # 짝이 맞으므로 pop.
            elif c == "]" and stack[-1] == "[":
                stack.pop()
            elif c == "}" and stack[-1] == "{":
                stack.pop()
            else:
                break
    else:   # for문이 break에 의해 끝나지 않고 끝까지 수행이 되면 모든짝이 맞아 떨어졌단 이야기.
        if not stack:
            result += 1 # 결과값 1 증가.

print(result)
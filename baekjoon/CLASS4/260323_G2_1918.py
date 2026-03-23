'''
G2 1918 후위 표기식

문제 설명:
후위표기법은 연산자가 피연산자 뒤에 위치하는 방법.
예로 a+b*c는 abc*+가 된다.

중위 표기식을 후위 표기식으로 바꾸는 방법은 주어진 중위 표기식을 연산자의
우선순위에 따라 괄호로 묶어준다.
그런 다음 괄호 안의 연산자를 괄호의 오른쪽으로 옮겨주면 된다.

예로, a+b*c는 (a+(b*c))의 식과 같게 된다.
그 다음 안에 있는 괄호의 연산자 *를 괄호 밖으로 꺼내게 되면 (a+bc*)가 된다.
마지막으로 또 +를 괄호 오른쪽으로 고치면 abc*+가 된다.

이 사실을 토대로 중위 표기식이 주어지면 후위 표기식으로 고치는 프로그램 작성하는 문제.

입력:
첫째 줄에 중위 표기식.
단 이 수식의 피연산자는 알파벳 대문자로 이루어지며, 수식에서 한 번씩만 등장.
그리고 -A+B와 같이 -가 앞에 오거나 AB와 같이 *가 생략되는 등의 수식은 없음.
표기식은 +, -, *, /, (, ) 로만 이루어짐. 길이는 100안넘음.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

a = input().strip()
dic = {'*':2, '/':2, '+':1, '-':1, '(':0}
stack = []

for i in a:
    if i == '(':
        stack.append(i)
    elif i == ')':
        while stack and stack[-1] != '(':
            a = stack.pop()
            output(a)
        stack.pop()
    elif i in dic:
        while stack and dic[stack[-1]] >= dic[i]:
            a = stack.pop()
            output(a)
        stack.append(i)
    else:
        output(i)

while stack:
    a = stack.pop()
    output(a)
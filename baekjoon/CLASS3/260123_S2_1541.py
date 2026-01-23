'''
S2 1541 잃어버린 괄호

문제 설명:
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

입력:
첫째 줄 - 식 - 0~9, +, - 만으로 이루어짐. 가장 처음, 마지막 문자는 숫자.
연속해서 두 개 이상의 연산자 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없음.
수는 0으로 시작가능.
입력으로 주어지는 식의 길이는 50보다 작거나 같음.

출력:
첫 줄 정답 출력
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

x = input().strip().split('-')

if '+' in x[0]:
    nums = map(int, x[0].split('+'))
    result = sum(nums)
else:
    result = int(x[0])

for i in x[1:]:
    if '+' in i:
        nums = map(int, i.split('+'))
        result -= sum(nums)
    else:
        result -= int(i)

output(str(result))
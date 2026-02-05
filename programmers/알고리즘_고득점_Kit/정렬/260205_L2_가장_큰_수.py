'''
L2 가장 큰 수

문제 설명:
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 구하는 문제.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성

제약:
numbers의 길이는 1 이상 100,000 이하
numbers의 원소는 0 이상 1,000 이하
정답이 너무 클 수 있으니 문자열로 바꾸어 return
'''

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True, key=lambda x: x * 3)
    answer = ''.join(numbers)
    return str(int(answer))
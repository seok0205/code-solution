'''
L2 소수 찾기

문제 설명:
한자리 숫자가 적힌 종이 조각이 흩어져있음. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 함

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성

제약:
numbers는 길이 1 이상 7 이하인 문자열
numbers는 0~9까지 숫자만으로 이루어져 있음
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미
'''

from itertools import permutations

def is_prime(num):
    n = int(num)
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    nums = set()
    cnt = 0
    
    for i in range(1, len(numbers)+1):
        p_nums = permutations(numbers, i)
        for k in p_nums:
            a = int(''.join(k))
            nums.add(a)
            
    for n in nums:
        if is_prime(n):
            cnt += 1
    return cnt
'''
B1 28702 FizzBuzz

다음 규칙에 따라 문자열을 한 줄에 하나씩 출력하는 문제

1. i가 3의 배수이면서 5의 배수이면 FizzBuzz 출력
2. i가 3의 배수이지만 5의 배수가 아니면 Fizz 출력
3. i가 3의 배수가 아닌데 5의 배수이면 Buzz 출력
4. i가 3의 배수도 아니고 5의 배수도 아니면 i 그대로 출력

연속으로 세개의 문자열이 주어지는데 이 다음에 올 문자열은 무엇인지 맞추는 문제.

ex)
Fizz, Buzz, 11 이면 다음은 12에 해당하는 Fizz가 나와야함.
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

num = 0

for _ in range(3):
    a = input()
    if a in ['Fizz', 'Buzz', 'FizzBuzz']:
        num += 1
        continue
    else:
        num = int(a) + 1

if num % 3 == 0 and num % 5 == 0:
    result = 'FizzBuzz'
elif num % 3 == 0 and num % 5 != 0:
    result = 'Fizz'
elif num % 3 != 0 and num % 5 == 0:
    result = 'Buzz'
else:
    result = num

print(result)
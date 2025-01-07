'''
하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성

제약 사항 :
자연수 N은 1부터 9999까지의 자연수이다.

ex :
input : 6789, output : 30
'''

N = input()

N = list(N)

result = 0

for i in N:
    result += int(i)

print(result)
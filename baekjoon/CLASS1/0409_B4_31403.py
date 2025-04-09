'''
B4 31403 A + B - C

문자열에서 '+'는 두 문자열을 이어붙이라는 의미, '-'는 양쪽 문자열을 수로 해석한 이후 빼라는 의미.
A, B, C를 각각 수와 문자열로 생각했을 때 A + B - C를 출력하는 문제
'''

A = int(input())
B = int(input())
C = int(input())

num1 = A + B - C
num2 = int(str(A) + str(B)) - C

print(num1)
print(num2)
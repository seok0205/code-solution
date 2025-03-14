'''
피보나치 수는 f(0) = 0, f(1) = 1일 때, 1 이상의 n에 대하여 f(n) = f(n-1) + f(n-2)가 적용되는 수.
2이 상의 n이 입력되었을 때, n번째 피보나치 수를 1234567로 나눈 나머지를 리턴하는 함수를 만드는 문제.
'''

n = 5
num_list = [0, 1]   # f(0)일때 0, f(1)일때 1

for i in range(2, n+1): # 2 이상의 수가 입력. n번째까지 반복.
    num_list.append(num_list[i-1] + num_list[i-2])  # f(n) = f(n-1) + f(n-2) 공식 표현.

print(num_list[-1] % 1234567) # n번째 수 1234567로 나눈 나머지 출력.
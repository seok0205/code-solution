'''
두 수의 최소공배수는 입력된 두 수의 배수 중 공통이 되는 가장 작은 수를 의미함.
예로 2와 7의 최소공배수는 14임. n개의 수의 최소공배수는 n개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됨.
n개의 숫자를 담은 배열 arr의 최소공배수를 구하는 문제.
'''

arr = [2, 6, 8, 14]

result = 0  # 최소공배수
count = 0

while True:
    count += 1
    lcm = max(arr) * count  # arr에서 가장 큰 수를 1부터 차례로 곱함

    a = 0   # 최소공배수 조건 만족하는 수의 개수
    for i in range(len(arr)):
        if lcm % arr[i] == 0:   # arr의 배수가 만약 lcm이라면 a가 1증가
            a += 1
        else:   # 배수가 아니라면 즉시 for문 종료.
            break
    
    if a == len(arr):   # a가 for문에서 모든 반복에 정상작동했다면 a가 arr의 길이만큼 1이 증가되었을 것.
        result = lcm    # 당시 lcm이 최소공배수가 됨.
        break

print(result)
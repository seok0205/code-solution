'''
자연수로 이루어진 원형 수열이 있음. 연속하는 부분 수열의 합의 경우의 수를 구하려함.
예로 [7, 9, 1, 1, 4]로 원형 수열을 만들면 처음 끝이 연결되어 있어 연속 부분이 많아짐.
합의 개수를 반환하라.

제한 사항 :
3 <= len(elements) <= 1000
1 <= elements[i] <= 1000

접근 :
1. result에 길이 1인 부분 수열 넣음.
2. 이전 구했던 결과 배열의 마지막 5개에 다음 인덱스의 값을 더함.(처음 넣은 result의 배열 수들이 단일 원소라서 합해가면 다른 부분합의 일부분이 될 수 있음.)
3. elements 길이만큼 반복한다.
4. set함수로 중복 제거 후 길이를 반환.
'''

elements = [7, 9, 1, 1, 4]

result = []

for i in elements:  # 1
    result.append(i)

for i in range(1, len(elements)):   # 3
    sum = []
    for j in range(len(elements), 0, -1):   # 2
        n_sum = result[-j] + elements[-j+i]
        sum.append(n_sum)
    for k in sum:
        result.append(k)

answer = len(set(result))   # 4

print(answer)
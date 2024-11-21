'''
2차원 행렬 arr1, arr2를 곱한 결과를 반환하는 문제.

제한 사항 :
2 <= len(arr1), len(arr2) <= 100
-10 <= arr[i][j] <= 20
곱할 수 있는 배열만 주어짐.

접근 :
1. 행렬의 곱은 arr1 * arr2 라면 result[0]은
result[0][0] = arr1[0][0]*arr2[0][0] + arr1[0][1]*arr2[1][0]
result[0][1] = arr1[0][0]*arr2[0][1] + arr1[0][1]*arr2[1][1]
의 형태로 계산된다. 다음으로 result[1]은
result[1][0] = arr1[1][0]*arr2[0][0] + arr1[1][1]*arr2[1][0]
result[1][1] = arr1[1][0]*arr2[0][1] + arr1[1][1]*arr2[1][1]
의 형태다.
2. 1을 보면 규칙이 있다.arr2의 곱하는 요소는 같은데 result의 인덱스가 1씩 증가할때, arr1의 곱하는 요소도 인덱스가 1이 증가한다.
3. 즉, arr1의 행, arr2의 열 끼리 곱함.
4. 배열에 곱한 것 저장.
'''

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

# 행렬 arr1, arr2의 행, 열의 수
r1, r2, c1, c2 = len(arr1), len(arr2), len(arr1[0]), len(arr2[0])
# 결과 저장 2차원 배열 초기화
result = [[0] * c1 for i in range(r1)]

# arr1의 행, arr2의 열끼리 곱해야함.
for i in range(r1):
    for j in range(c2):
        for k in range(c1): # 두 행렬 요소의 곱을 결과 배열에 더함.
            result[i][j] += arr1[i][k] * arr2[k][j] # 1번 접근 과정에서 얻은 규칙
    
print(result)
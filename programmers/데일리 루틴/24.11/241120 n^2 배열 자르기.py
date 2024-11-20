'''
정수 n, left, right가 주어지고 아래 순서대로 1차원 배열을 만들려고 함.
1. n행 n열 크기의 비어있는 2차원 배열을 만듦.
2. i = 1, 2, 3... , n에 대해 다음 과정을 반복.
    - 1행 1열부터 i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채움.
3. 1행, 2행, ... n행을 잘라내어 모두 이어붙인 새로운 1차원 배열 만듦.
4. 새로운 1차원 배열을 arr이라 할 때, arr[left], arr[left+1], ..., arr[right]만 남기고 나머지는 지움.
만들어진 1차원 배열 반환하라.

제한 사항 :
1 <= n <= 10**7
0 <= left <= right < n**2
right - left < 10**5

접근 :
1. 숫자가 대입되는 규칙을 보면 0,0이면 1, 두 인덱스 중 하나라도 1이 들어가면 2, 2가 하나라도 들어가면 3임.
2. 열이 1인 행렬로 생각한다면 
0(0,0) 1(0,1) 2(0,2) 3(1,0) 4(1,1) 5(1,2) 6(2,0) 7(2,1)	8(2,2)이 순서.
3. n이 3이니까 n으로 해당 인덱스를 나눴을 때 몫과 나머지에 따라 숫자가 들어가는 것을 알 수 있다.
4. 따라서 0(0,0) 1(0,1) 2(0,2) 1(1,0) 1(1,1) 2(1,2) 2(2,0) 2(2,1), 2(2,2)이 된다. 여기에 1만 더한다면 답이 된다.
'''

n = 4
left = 7
right = 14

''' 시간 초과
result = [[i for i in range(n)] for j in range(n)]

for i in range(n):
    cnt = i+1
    for j in range(n):
        if j > i:
            cnt += 1
            result[i][j] = cnt
        else:
            result[i][j] = cnt

x = sum(result, [])

print(x[left:right+1])
'''

result = []
for i in range(left, right+1):
    a = i // n  # 몫
    b = i % n   # 나머지
    if a < b:   # 몫과 나머지 중 큰 값을 a에 넣기 위해서.
        a, b = b, a
    result.append(a+1)

print(result)
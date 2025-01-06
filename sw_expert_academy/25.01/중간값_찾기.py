'''
중간값은 통계 집단의 수치를 크기 순으로 배열했을 때 전체의 중앙에 위치하는 수치를 뜻함.
입력으로 N개의 점수가 주어졌을 때, 중간값을 출력하라.

조건 :
N은 항상 홀수.
N은 9이상 199이하의 정수.

접근 방법:
1. 입력받은 수들을 리스트형태로 저장.
2. 오름차순으로 저장.
3. N은 홀수이니까 정중앙의 인덱스에 위치한 수 도출.
'''

N = int(input())
a = list(map(int, input().split()))
    
a.sort()
    
result = a[N//2]
print(result)

'''
sort() 미사용 시,

for i in range(N // 2 + 1):
    for j in range(1, N - i):
        if (a[j - 1] > a[j]):
            num = a[j-1]
            a[j-1] = a[j]
            a[j] = num
'''
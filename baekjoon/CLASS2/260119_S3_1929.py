'''
1929 S3 소수 구하기

문제 설명:
M 이상 N 이하의 소수를 모두 출력하는 프로그램 작성

입력:
첫째 줄에 자연수 M, N이 빈 칸 두고 주어짐. (1 <= M <= N <= 1,000,000)
M 이상 M이하의 소수가 하나 이상 있는 입력만 주어짐

출력:
한 줄에 하나씩, 증가하는 순서대로 소수 출력
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

M, N = map(int, input().split())

def solution(M, N):
    nums = [1 for _ in range(N+1)]
    p = 2
    while (p**2 <= N):
        if nums[p]:
            for i in range(p**2, N+1, p):
                nums[i] = 0
        p += 1
    nums = [p for p in range(M, N+1) if nums[p] and p != 1]

    for j in nums:
        print(j)

solution(M, N)
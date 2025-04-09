'''
S3 2559 수열

매일 측정한 온도가 정수의 수열로 주어질 때, 연속적인 며칠 동안의 온도의 합이 가장 큰값인지 계산하는 문제

입력:
두 개의 정수 N, K가 주어짐(N은 온도 측정한 전체 날짜, K는 합을 구하기 위한 연속적인 날짜)
K는 1과 N사이의 정수. 둘째 줄에는 매일 측정한 온도를 나타내는 N개의 정수 주어짐. 모두 -100 이상 100이하

출력:
입력되는 온도의 수열에서 연속적인 K일의 온도의 합이 최대가 되는 값 출력
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

N, K = map(int, input().split())
temparature = list(map(int, input().split()))
sub = 0

for i in range(K):              # 첫날부터 K날까지의 합을 최댓값으로 정해놓고 시작
    sub += temparature[i]

result = sub

for i in range(K, N):           # 첫날빼고, K+1날의 온도더하고, 두번째날 빼고, K+2날 온도더하고를 반복
    sub += temparature[i]       # K날씩 일일히 더하는 것보다 훨씬 효율적. 처음에 이중 반복문으로 시도해서 시간초과!
    sub -= temparature[i-K]
    
    result = max(result, sub)   # 최댓값 비교

print(result)
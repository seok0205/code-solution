'''
S3 27922 현대모비스 입사 프로젝트

문제 설명:
효율적 공부를 위해 강의 N개를 찾음.
그 중 i번째 강의는 세 종류의 역량을 a, b, c 증가시켜줌.

N개의 강의를 모두 수강하고 싶지만, K개의 강의만 골라 수강하려함.
시간이 촉박해 세 종류 역량을 모두 기르기 힘들다고 판단해 두 가지 역량만 최대화 시키려 함.

N개의 강의중 K개의 강의를 수강했을 때 얻을 수 있는 두 종류의 역량의 합의 최댓값을 구해주자.

입력:
첫 줄 - 강의 총 개수 N, 수강할 강의 개수 K가 주어짐. (1 <= K <= N <= 100,000)
두번째 줄부터 N+1줄까지, i+1번째 줄에 i번째 강의 들었을 때 증가하는 a, b, c가 구분되어 정수로 주어짐. 각각 0보다 크고 10,000보다 작음.

출력:
K개의 강의를 수강했을 때 얻을 수 있는 두 종류의 역량의 합의 최댓값 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
classes = [list(map(int, input().split())) for _ in range(N)]
result = 0

def find(a, b, k, classes):
    classes.sort(key=lambda x: x[a]+x[b], reverse=True)
    temp = 0
    for i in range(k):
        temp += (classes[i][a] + classes[i][b])
    return temp


for a, b in [(0, 1), (0, 2), (1, 2)]:
    new = find(a, b, K, classes)

    result = max(new, result)

print(result)
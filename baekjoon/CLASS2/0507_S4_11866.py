'''
S4 11866 요세푸스 문제 0

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K가 주어짐(N보다 작거나 같음)
순서대로 K번째 사람을 제거. 한사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나감.
N명의 사람이 모두 제거될 때까지 계속됨.
원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라함.
예로 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>임

N, K가 주어질때 요세푸스 순열을 구하는 문제
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

from collections import deque


def change():           # 한칸씩 이동. 앞에있던사람은 뒤로.
    a = q.popleft()
    q.append(a)


N, K = map(int, input().split())
q = deque([i for i in range(1, N+1)])       # 모든 사람 인큐해서 시작
result = list()

while q:
    for _ in range(K-1):            # K-1번 옮기면 K번째 뒷사람이 맨 앞으로 오게됨
        change()
    
    result.append(q.popleft())      # 제거

result_string = ", ".join(map(str, result))     # 결과 출력

print(f"<{result_string}>")
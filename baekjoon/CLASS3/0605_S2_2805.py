'''
S2 2805 나무 자르기

나무 M미터 필요.
목재 절단기의 동작 방식은 이러하다.
절단기를 높이 H를 지정해야 함. 높이 지정 시, 톱날이 땅으로부터 H미터 위로 올라감.
한 줄에 연속해있는 나무를 모두 절단해버림.

따라서, 높이가 H보다 큰 나무는 H위의 부분이 잘릴 것이고, 낮은 나무는 잘리지 않을 것임.
예로, 20, 15, 10, 17의 나무가 있으면 H를 15로 정했을 때, 15, 15, 10, 15가 되고, 길이 5, 2인 나무를 획득.
절단기에 설정할 수 있는 높이는 양의 정수 혹은 0.
꼭 나무를 필요한 만큼만 가져가려고 함. 적어도 M미터의 나무를 가져가기 위해 절단기에 설정할 수 있는 최댓값을 구하는 문제

입력:
첫 줄 N, M - 나무 수, 획득하려는 나무 길이
둘째 줄 나무의 높이. 나무 높이 합은 항상 M보다 크거나 같음
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline


def get_wood(s, e):     # 나무 자르기 이분탐색
    global result

    if s > e:           # 시작점이 더 커지면 그만 이전 구한 최댓값으로 답 설정
        return

    new_tree = (s + e) // 2     # 중간길이로 설정
    sub = 0

    for i in range(N):          # 나무 별로 잘라서 값을 sub에 누적시킴
        if trees[i] <= new_tree:
            continue

        sub += (trees[i] - new_tree)

        if sub > M:         # 이미 원하는 길이보다 커지면 중단
            break

    if sub < M:             # 못미치면 길이를 좀더 낮춰서 더많이 깎기
        get_wood(s, new_tree-1)
    elif sub > M:           # 오버되면 길이 좀더 높여서 덜 깎기
        result = new_tree       # 길이 못맞출 경우 대비해서 저장해놓기. 왜냐하면 M만큼은 깎아야 하므로.
        get_wood(new_tree+1, e)
    else:                   # M과 같으면 그대로 길이 저장 후 종료.
        result = new_tree
        return


N, M = map(int, input().split())
trees = list(map(int, input().split()))
result = 0
trees.sort(reverse=True)    # 높은 길이 순으로 정렬
get_wood(0, trees[0])       # 가장 높은 나무로 끝값 설정후 이분탐색 시작

print(result)
'''
모의 SW 역량테스트 4012 요리사

두 명의 손님에게 음식 제공하려고 함
두 손님은 식성이 비슷해 최대한 비슷한 맛의 음식을 만들어야 함
N개의 식재료.
식재료들을 각각 N/2개씩으로 나누어 두 개의 요리를 하려고 함 N은 짝수.

이때 각각 음식을 A, B라고 함
비슷한 음식 만들기 위해선 A, B 음식 맛이 최소가 되도록 재료 배분해야함
음식 맛은 음식 구성 재료 조합 따라 다름

식 재료 i, j는 같이 요리하면 궁합이 잘맞아 시너지 S가 발생
각 음식 맛은 음식 구성 재료들이 발생시키는 시너지 S들의 합

식재료 i를 식재료 j와 같이 요리하게 되면 발생하는 시너지 S의 정보가 주어지고,
가지고 있는 식재료를 이용해 A, B음식을 만들 때, 두 음식 간 맛의 차이가 최소가
되는 경우를 찾고 그 최솟값을 정답 출력
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def cook(cnt, idx):                 # 식재료 최소 차 구하는 함수, cnt : 재료 선택 횟수, idx : 선택해나가야하는 재료들
    global result
    
    if cnt == N//2:                 # 식재료를 N의 절반 선택했다면, 서로 비교를 해줘야함
        p1.clear()                  # A식재료 p1, B식재료 p2 초기화
        p2.clear()
        for k in range(N):          # used의 0, 1 값대로 A, B 식재료 리스트에 추가
            if used[k]:
                p1.append(k)
            else:
                p2.append(k)
        p1_score = score_synergy(p1)    # 각 요리의 점수 구하기
        p2_score = score_synergy(p2)
        if abs(p1_score - p2_score) < result:       # 점수 차 절댓값과 현재 최댓값 비교 후 더 큰 것으로 대체
            result = abs(p1_score - p2_score)
        return
    
    for i in range(idx, N):         # A, B 식재료 각각 분배하는 부분집합 구하기
        if not used[i]:             # 사용하지 않은 식재료라면 한번 넣어 보기
            used[i] = 1             # 사용
            cook(cnt + 1, i + 1)    # 식재료를 하나 더 선택했으니 다음 선택을하러 넘어감 이때까지 선택해왔던 재료들은 필요 없으므로 i+1을 idx로 설정
            used[i] = 0             # 사용 취소
    

def score_synergy(lst):             # 점수 구하기
    score = 0
    for i in range(N//2):           # 리스트 모두 돌면서
        for j in range(i+1, N//2):  # 모든 짝이 될 수 있는 숫자들 구해서 synergy 표에서 해당 좌표들 값 더해주기
            score += synergy[lst[i]][lst[j]] + synergy[lst[j]][lst[i]]
    return score


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    
    used = [0] * N
    p1 = []
    p2 = []
    result = float("inf")
    
    cook(0, 0)
    
    print(f'#{tc} {result}')
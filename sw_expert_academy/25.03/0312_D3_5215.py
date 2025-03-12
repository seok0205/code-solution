'''
D3 5215 햄버거 다이어트

나의 햄버거 재료에 대한 점수와 가게에서 제공하는 재료에 대한 칼로리가 주어질 때,
좋아하는 햄버거를 먹으면서도 다이어트에 성공할 수 있도록 정해진 칼로리 이하의
조합 중에서 내가 가장 선호하는 햄버거를 조합해주는 프로그램 제작.

단, 여러 재료를 조합하였을 햄버거의 선호도는 조합된 재료들의 맛에 대한 점수의 합으로 결정,
같은 재료를 여러 번 사용 불가능, 햄버거의 조합의 제한은 칼로리 제외하고 없음
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def make_hamburger(idx, cur_score, kcal):
    global max_score
    
    if L >= kcal:           # 일정 칼로리 이상이면 함수 종료, 이하면 최대 점수와 비교
        if cur_score > max_score:
            max_score = cur_score
    else:
        return
    
    if False not in used:       # 재료 다썼으면 재귀 그만
        return
    
    for i in range(idx, N):     # idx부터 뒷 자리까지
        if used[i]: continue        # 만약 재료 쓴상태면 다음 반복 실행
        
        used[i] = True              # 해당 재료 True로 만들고
        score = cur_score + t_lst[i]        # 점수 갱신
        make_hamburger(i, score, kcal + k_lst[i])       # 재귀 호출, 점수와 칼로리 갱신한 상태로
        used[i] = False             # 재귀 호출 끝나면 안 쓴상태로 복귀
    

T = int(input())

for tc in range(1, T+1):
    N, L = map(int, input().split())
    
    t_lst = []
    k_lst = []
    max_score = 0       # 최대 점수
    used = [False] * N      # 재료를 썼는가 안썼는가 확인
    
    for _ in range(N):
        T, K = map(int, input().split())
        t_lst.append(T)
        k_lst.append(K)
        
    make_hamburger(0, 0, 0)
    
    print(f'#{tc} {max_score}')
'''
모의 SW 역량테스트 4008 숫자 만들기

N개의 숫자가 적혀 있는 게임 판이 있고, +, -, x, /의 연산자 카드를 숫자 사이에 끼워 넣어
다양한 결과값 구해보려 함
수식 계산 시, 연산자의 우선 순위는 고려 X, 왼쪽에서 오른쪽으로 차례대로 계산

주어진 연산자 카드를 사용하여 수식을 계산했을 때 그 결과가 최대가 되는 수식과
최소가 되는 수식을 찾고 두 값의 차이를 출력
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def cal(idx, used, result):
    global min_result, max_result
    
    if idx == N:                        # 마지막 수까지 계산했으면 최대, 최솟값 비교 후 결정
        if min_result > result:
            min_result = result
        if max_result < result:
            max_result = result
        return
    
    if used[0]:                         # 인덱스 0부터 3 까지 차례로 +, -, *, /임
        used[0] -= 1                    # 주어진 개수가 담긴 리스트 주어지므로 확인후 횟수 남아있으면 연산 실행
        cal(idx + 1, used, result + numbers[idx])
        used[0] += 1
    
    if used[1]:
        used[1] -= 1
        cal(idx + 1, used, result - numbers[idx])
        used[1] += 1
    
    if used[2]:
        used[2] -= 1
        cal(idx + 1, used, result * numbers[idx])
        used[2] += 1
        
    if used[3]:
        used[3] -= 1
        if result < 0:
            result = -(abs(result) // numbers[idx])     # 음수 계산 시 절대값으로 먼저 몫을 구해준후 음수 표현으로 바꾸기
        else:
            result //= numbers[idx]
        cal(idx + 1, used, int(result))
        used[3] += 1


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tools = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    min_result = 100000000      # 최대 최솟값 기본값 설정 계산 범위가 음양 1억을 넘지 않음
    max_result = -100000000
    
    cal(1, tools, numbers[0])
    
    print(f'#{tc} {max_result - min_result}')
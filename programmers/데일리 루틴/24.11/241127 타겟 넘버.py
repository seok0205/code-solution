'''
n개의 음이 아닌 정수들이 있음. 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 함.
예로, [1, 1, 1, 1, 1]로 숫자 3을 만드려면 다섯가지 방법이 있다.
1. -1+1+1+1+1 = 3
2. +1-1+1+1+1 = 3
3. +1+1-1+1+1 = 3
4. +1+1+1-1+1 = 3
5. +1+1+1+1-1 = 3
사용할 수 있는 숫자 배열 numbers, 타겟 넘버 target이 주어졌을 때, 타겟 넘버 만드는 방법 수를 반환하라.

제한 사항 :
주어지는 숫자 개수는 2개 이상 20개 이하.
각 숫자는 1이상 50이하.
타겟 넘버는 1이상 1000이하 자연수

접근 :
1. 재귀함수로 접근.(스택 및 큐로도 접근 가능.)
2. dfs 함수를 만든다면, 특정 순서 숫자마다 빼기와 더하기 부호 모두 계산하는 경우의 수를 탐색.
3. 마지막 원소일때, 최종 합이 target과 같다면 answer 값 1 증가.
'''

numbers = [4, 1, 2, 1]
target = 4

answer = 0  # 답(식의 경우의 수)

def dfs(idx, result):   # dfs 함수
    global answer   # 전역변수 사용
    if idx == len(numbers):    # 인덱스가 numbers의 마지막이고,
        if result == target:    # result(총합)이 target과 같으면
            answer += 1 # 조건 만족 경우의수 1 증가.
        return
    else:
        dfs(idx+1, result+numbers[idx]) # +부호 일때
        dfs(idx+1, result-numbers[idx]) # -부호 일때

dfs(0,0)    # 재귀 함수 실행.

print(answer)
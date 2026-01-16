'''
S4 2839 설탕 배달

문제 설명:
설탕공장에서 설탕을 사탕가게에 N킬로그램을 배달해야함
봉지는 3킬로 봉지, 5킬로 봉지가 있음

귀찮아서 최대한 적은 봉지를 가져가려함. 18킬로 설탕 배달 시에, 3키로 6개도 되지만,
개수로는 5키로 3개 3킬로 하나가 제일 적은 개수의 봉지 배달임

상근이가 정확히 N킬로그램 배달해야 할때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 문제

입력: 첫째 줄에 N
출력: 상근이가 배달하는 봉지의 최소 개수 출력 그런데 N킬로그램을 만들 수 없으면 -1 출력
'''

# import sys
# sys.stdin = open('tc.txt')

N = int(input())
result = 2000

for i in range((N//5)+1):
    for j in range((N//3)+1):
        if N == (5*i)+(3*j):
            cnt = i+j
            result = min(result, cnt)
            break

if result == 2000:
    result = -1

print(result)
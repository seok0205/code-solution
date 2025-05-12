'''
S4 1764 듣보잡

누군가가 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 문제

입력:
N, M: 듣도못한사람 수, 보도못한사람 수
N개 줄동안 듣도 못한 사람 이름
N+2째 줄부터 M개 줄동안 보도 못한 사람 이름. 길이는 20이하.
N, M은 500000이하의 자연수.

듣도 못한 사람의 명단에는 중복되는 이름 없음. 보도 못한 사람의 명단도 마찬가지.
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

N, M = map(int, input().split())

no_heard_no_seen = dict()       # 사람 이름과 횟수 담을 딕셔너리
cnt = 0                         # 같이 명단에 들어있는 수

for _ in range(N):
    string = input().lower()            # 대문자 입력으로 정렬시에 뒤바뀌는것 방지
    no_heard_no_seen[string] = 0        # 딕셔너리에 값을 0으로 담기

for _ in range(M):
    string = input().lower()
    if string in no_heard_no_seen.keys():       # 키에 존재한다면, 해당 값 1 증가
        no_heard_no_seen[string] += 1
        cnt += 1            # 두 곳 모두 적혀져 있는 것. 1 증가.

print(cnt)          # 같이 들어있는 사람 수 먼저 출력.
result = []         # 값이 1인 사람 리스트에 담기
for name, count in no_heard_no_seen.items():
    if count == 1:
        result.append(name)

result.sort()       # 정렬하여 사전순으로 나열한뒤에

for i in result:
    print(i)        # 이름 출력
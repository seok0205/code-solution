'''
G4 1043 거짓말

문제 설명:
사람 수 N이 주어짐.
그 이야기의 진실을 아는 사람도 주어짐.
각 파티에 오는 사람들의 번호가 주어짐. 난 모든 파티에 참가해야함.
이때, 내가 지민이가 거짓말쟁이로 알려지지 않으면서, 거짓말을 할 수 있는 파티 개수의 최댓값 구하는 문제.

입력:
첫째 줄 - N, M (사람 수, 파티 수)
둘째 줄 - 이야기 진실을 아는 사람의 수와 번호.
진실을 아는 사람 수가 먼저 주어지며, 개수만큼 번호가 주어짐.
사람 번호는 1부터 N
셋째 줄 - M개 줄에 각 파티마다 오는 사람의 수 번호가 둘째 줄과 같은 방식으로 주어짐.
N과 M은 50 이하 자연수, 진실 아는 사람수는 0이상 50이하의 정수, 각 파티마다 오는 사람 수는 1이상 50이하의 정수.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

N, M = map(int, input().split())

data = list(map(int, input().split()))
know_person = data[0]
know_person_list = data[1:]

party_list = []
for _ in range(M):
    data_party = list(map(int, input().split()))
    party_person_list = data_party[1:]
    party_list.append(party_person_list)
    
parent = [i for i in range(N+1)]


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for party in party_list:
    person = party[0]
    for i in range(1, len(party)):
        union(parent, person, party[i])

if not know_person:
    output(str(M))
else:
    roots = set()
    for person in know_person_list:
        roots.add(find(parent, person))

    answer = 0

    for party in party_list:
        lie = True
        for person in party:
            if find(parent, person) in roots:
                lie = False
                break
        
        if lie:
            answer += 1
    
    output(str(answer))
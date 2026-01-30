'''
G4 9019 DSLR

문제 설명:
4개의 명령어 D,S,L,R을 이용한 계산기.
레지스터가 하나 있는데, 0이상 10,000 미만의 십진수를 저장 가능.
각 명령어는 이 레지스터에 저장된 n을 다음과 같이 변환(네 자릿수를 d1, d2, d3, d4라 할때)

1. D : n을 2배로 바꿈. 9999보다 크 경우 10000으로 나눈 나머지 취함. 그 결과 값(2n mod 10000)을 레지스터에 저장.
2. S : n에서 1을 뺀 결과 n-1을 레지스터에 저장. n이 0이면 9999가 대신 레지스터에 저장.
3. L : n의 각 자릿수를 왼편으로 회전, 레지스터에 저장. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 됨.
4. R : n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 됨.

L, R 명령어는 십진 자릿수를 가정하고 연산 수행. 예로 n이 1234 일때, L을 적용하면 2341이 되고 R을 하면 4123이 됨.
작성할 프로그램은 다른 정수 A, B에 대해 A를 B로 바꾸는 최소한의 명령어를 생성하는 프로그램. 

n의 자릿수로 0이 포함된 경우에 주의해야 함. 예로 1000에 L을 적용하면 0001이 되므로 결과는 1이 됨. 하지만 R을 적용하면 0100이 되므로 결과는 100이 됨.

입력:
T개의 TC로 구성.
각 TC는 A, B가 공백으로 분리되어 주어짐. A는 레지스터의 초기값을 나타내고, B는 최종값을 나타냄. A, B는 모두 0이상 10,000 미만임.

출력:
A를 B로 바꾸기 위한 최소한의 명령어 나열을 출력. 가능한 명령어 나열이 어러가지면, 아무거나 출력.
'''

import sys
from collections import deque
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.read
output = sys.stdout.write


def solution():
    data = input().split()

    T = int(data[0])
    idx = 1
    results = []
    for _ in range(T):
        A, B = int(data[idx]), int(data[idx+1])
        idx += 2

        parent = [-1] * 10000
        command = [''] * 10000
        visit = [0] * 10000
        
        q = deque([A])
        visit[A] = 1
        while q:
            x = q.popleft()

            if x == B:
                break

            nx = (x * 2) % 10000
            if not visit[nx]:
                visit[nx] = 1
                parent[nx] = x
                command[nx] = 'D'
                q.append(nx)
                if nx == B:
                    break

            nx = (x - 1) % 10000
            if not visit[nx]:
                visit[nx] = 1
                parent[nx] = x
                command[nx] = 'S'
                q.append(nx)
                if nx == B:
                    break
            
            nx = (x % 1000) * 10 + (x // 1000)
            if not visit[nx]:
                visit[nx] = 1
                parent[nx] = x
                command[nx] = 'L'
                q.append(nx)
                if nx == B:
                    break
            
            nx = (x % 10) * 1000 + (x // 10)
            if not visit[nx]:
                visit[nx] = 1
                parent[nx] = x
                command[nx] = 'R'
                q.append(nx)
                if nx == B:
                    break
        
        result = []
        now = B
        while now != A:
            result.append(command[now])
            now = parent[now]
        results.append(''.join(result[::-1]))

    output('\n'.join(results) + '\n')


if __name__ == "__main__":
    solution()
'''
S2 11279 최대 힙

자료구조 최대 힙 이용해서 연산 프로그램 작성
1. 배열에 자연수 x 넣음
2. 배열에서 가장 큰 값 출력, 그 값을 배열에서 제거
비어있는 배열에서 시작

입력:
첫째줄 - N (1~100,000)
다음 N개의 줄 - 연산 정보 x
x가 자연수면 배열에 x 값 추가, 0이면 배열에서 가장 큰값 출력 후, 삭제
입력 자연수는 2의 31승보다 작음

출력:
0이 주어진 횟수만큼 답 출력. 배열 비어있는데 0이나오면 0출력
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

N = int(input().strip())
seq = [0]

for _ in range(N):
    n = int(input().strip())

    if n:
        seq.append(n)
        idx = len(seq) - 1
        while idx > 1:
            p = idx // 2
            if seq[idx] > seq[p]:
                seq[idx], seq[p] = seq[p], seq[idx]
                idx = p
            else:
                break
    else:
        if len(seq) > 1:
            num = seq[1]
            
            if len(seq) == 2:
                seq.pop()
            else:
                seq[1] = seq.pop()

                idx = 1
                while idx * 2 < len(seq):
                    large_c = idx * 2
                    if large_c + 1 < len(seq) and seq[large_c + 1] > seq[large_c]:
                        large_c += 1
                    
                    if seq[idx] < seq[large_c]:
                        seq[idx], seq[large_c] = seq[large_c], seq[idx]
                        idx = large_c
                    else:
                        break
            output(str(num) + '\n')
        else:
            output('0' + '\n')
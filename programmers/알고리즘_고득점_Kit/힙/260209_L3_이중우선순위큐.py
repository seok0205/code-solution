'''
L3 이중우선순위큐

문제 설명:
이중 우선순위 큐는 다음 연산을 할 수 있는 자료구조를 말합니다.

I '숫자' : 큐에 주어진 숫자를 삽입합니다.
D 1 : 큐에서 최댓값을 삭제합니다.
D -1 : 큐에서 최솟값을 삭제합니다.

이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때, 모든 연산을 처리한 후 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return 하도록 solution 함수를 구현해주세요.

제약:
operations는 길이가 1 이상 1,000,000 이하인 문자열 배열입니다.
operations의 원소는 큐가 수행할 연산을 나타냅니다.
원소는 “명령어 데이터” 형식으로 주어집니다.- 최댓값/최솟값을 삭제하는 연산에서 최댓값/최솟값이 둘 이상인 경우, 하나만 삭제합니다.
빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시합니다.
'''

import heapq

def solution(operations):
    answer = []
    max_q = []
    min_q = []
    num_dic = dict()
    for operation in operations:
        command, num = operation.split()
        
        if command == 'I':
            heapq.heappush(min_q, int(num))
            heapq.heappush(max_q, -int(num))
            if num not in num_dic:
                num_dic[num] = 1
            else:
                num_dic[num] += 1
                
        elif command == 'D':
            if num == '1':
                while max_q:
                    new_num = heapq.heappop(max_q)
                    if num_dic[str(-new_num)]:
                        num_dic[str(-new_num)] -= 1
                        break
            else:
                while min_q:
                    new_num = heapq.heappop(min_q)
                    if num_dic[str(new_num)]:
                        num_dic[str(new_num)] -= 1
                        break
    
    while max_q and num_dic[str(-max_q[0])] == 0:
        heapq.heappop(max_q)
        
    while min_q and num_dic[str(min_q[0])] == 0:
        heapq.heappop(min_q)
    
    if max_q and min_q:
        answer.append(-max_q[0])
        answer.append(min_q[0])
    else:
        return [0,0]
    return answer
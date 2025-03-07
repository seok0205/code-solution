'''
D2 22149 출입 감시

모든 사람들에게 정수로 된 id 부여, 건물에 출입시, 해당 사람이 부여받은 id 저장,
나중에 검사해서 id가 두 번 나왔다면 해당 사람은 건물에 들어왔다 나간것,
한번만 나오면 아직 나가지 않은 것.
아직 나가지 않은 사람이 1명 남아 있다고 가정했을 때, 그 사람 id 알아내는 문제
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ids = list(map(int, input().split()))
    
    num = 0
    
    for i in range(len(ids)):       # XOR 비트연산자는 2번 하면 같은값으로 되돌아옴.
        num = ids[i] ^ num          # 0인 num에 같은 수로 2번 XOR연산한다면 0이될것임. 1번만 id가 등장하면 그 수만 한번 연산하기에 그 수가 나옴.
        
    print(f'#{tc} {num}')
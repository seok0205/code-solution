'''
S4 1620 나는야 포켓몬 마스터 이다솜

포켓몬 도감에서 포켓몬의 이름을 보면 포켓몬 번호를 말하거나,
포켓몬 번호를 보면 포켓몬의 이름을 말하는 연습해야함

입력:
첫째 줄에 도감에 수록되어 있는 포켓몬 개수 N이랑 맞춰야하는 문제 개수 M이 주어짐.
N, M은 1보다 크거나 같고, 100,000보다 작거나 같음(자연수)
둘째 줄부터 N개의 줄에 1번인 포켓몬부터 N번 포켓몬까지 입력됨.
첫글자만 대문자, 나머지는 소문자. 일부는 마지막만 대문자일수도 있음.
최대 길이 20, 최소 2.
그 다음줄부터는 M개의 줄에 맞춰야하는 문제가 입력으로 들어옴.
알파벳으로 들어오면 포켓몬 번호, 번호로 들어오면 이름으로 출력.
입력은 반드시 1보다 크거나 같고, 입력은 도감에 있는 애들만 나옴.

출력:
M개의 줄에 문제에 대한 답을 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())

pocketmon_name_dict = dict()
pocketmon_num_dict = dict()

for i in range(1, N+1):
    name = input().strip()
    pocketmon_name_dict[i] = name
    pocketmon_num_dict[name] = i 

num = '0123456789'

for _ in range(M):
    question = input().strip()
    if question[0] in num:
        idx = int(question)
        print(pocketmon_name_dict.get(idx) + '\n')
    else:
        print(str(pocketmon_num_dict.get(question)) + '\n')
'''
S5 10814 나이순 정렬

온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어짐. 이 때, 회원들을 나이가 증가하는 순으로,
나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 문제

입력:
N : 회원 수
둘째 줄부터는 회원의 나이, 이름 공백으로 주어짐.
나이는 1보다 크거나 같고 200보다 작거나 같은 정수. 이름은 알파벳 대소문자로 이루어져있고, 100보다 작거나같은 문자열.
입력은 가입한 순서.
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

N = int(input())

user_list = list()

for _ in range(N):          # 유저 정보 입력 받기
    age, name = map(str, input().split())
    age = int(age)
    user_list.append((age, name))

user_list.sort(key=lambda x: x[0])      # 나이 기준으로 정렬, 어차피 입력받은건 가입일 순서. 이므로 나이순으로 정렬하면 자연스럽게 가입일 순서가 차등으로 대입.

for i in user_list:
    print(f"{i[0]} {i[1]}")     # 출력
'''
MBTI와 같은 성격 유형 검사를 만드는 문제. survey에는 질문의 성향검사를 뜻하는 제시어가 나온다. 각각 R과 T, C와 F, J와 M, A와 N을 검사한다.
survey의 요소중 'RT'가 제시 된다면, 인덱스가 작은 쪽의 답을 하면 R에 점수를, 인덱스가 큰 쪽의 답을 하면 T의 점수를 부여한다.
choices는 질문자의 답안을 뜻하고, 1부터 7까지의 답이 있으며, 4는 0점을 뜻한다(중립)
점수가 같게 나온다면 알파벳 순으로 빠른 글자를 도출한다.
'''

survey = ['AN', 'CF', 'MJ', 'RT', 'NA']
choices = [5, 3, 2, 7, 5]

result = '' # 성격 분석 결과
dic = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}  # 딕셔너리로 설문을 통해 성향별 얻은 점수를 기록.
score = [3, 2, 1, 0, 1, 2, 3]   # 점수. 7가지. 비동의부터 동의까지.

for i in range(len(survey)):
    one, two = survey[i][0], survey[i][1]   # survey의 요소, 예로 AN이면 one이 A, two가 N.
    if choices[i] <= 3: # 고른 답이 3보다 같거나 작으면
        dic[one] += score[choices[i]-1] # 예로 들었던 A에 증가.
    elif choices[i] > 4:    # 고른 답이 4보다 크면
        dic[two] += score[choices[i]-1] # N에 증가. 4는 중립의 답이므로 어느 항목도 점수 받지 않는다.

print(dic)

if dic['R'] >= dic['T']:    # R,T 중 점수 높은 것 출력. 같을때 R이 나오는 이유는 만약에 점수가 같으면 알파벳 상 순서가 빠른 R이 도출. 이하동문.
    result += 'R'
else:
    result += 'T'

if dic['C'] >= dic['F']:
    result += 'C'
else:
    result += 'F'

if dic['J'] >= dic['M']:
    result += 'J'
else:
    result += 'M'

if dic['A'] >= dic['N']:
    result += 'A'
else:
    result += 'N'

print(result)
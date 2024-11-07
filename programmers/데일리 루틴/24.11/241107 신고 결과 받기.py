'''
불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템에 대한 문제.
한 번에 한 명의 유저를 신고할 수 있고, report에 "신고자ID, 신고당한ID" 형태로 저장된다.
id_list에 유저들의 명단이 있고, k번 이상 신고당하면 정지 ID로 뜬다. 정지ID로 선정되면 해당 유저를 신고한 유저들에게 처리 결과 메세지가 전송된다.
id_list 유저들의 순서대로 처리 결과 메세지 수신 횟수를 구하는 문제이다.
(똑같은 유저가 똑같은 유저를 신고하면 신고 횟수에 포함되지 않는다.)
'''

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

reported_cnt_dic = {}
user_dic = {}
result = []

report = list(set(report)) # 동일 신고 제거.

for i in id_list:   # 딕셔너리에 유저마다 신고한 아이디들 저장.
    user_dic[i] = []

for i in id_list:   # 딕셔너리에 유저마다 신고당한 횟수를 저장.
    reported_cnt_dic[i] = 0

for i in report:    # 신고 내역들을 딕셔너리에 추가.
    person = i.split()  # 공백으로 신고한 ID, 신고당한 ID 분리.
    user_dic[person[0]].append(person[1])   # 신고한 ID의 키값에 신고당한 ID 추가.
    reported_cnt_dic[person[1]] += 1    # 신고당한 ID의 키값(신고당한 횟수)에 1 증가.

for i in id_list:   # 위에서 완성된 딕셔너리 통해 메시지 수신 횟수 도출.
    cnt = 0 # 수신 횟수
    for j in user_dic[i]:   # 해당 유저가 신고한 유저가 만약,
        if reported_cnt_dic[j] >= k:    # 신고당한 횟수가 k 이상일때,
            cnt += 1    # 처리 결과 수신
    result.append(cnt)  # id_list에 저장된 이름 순서대로 진행되므로 순서대로 추가.

print(reported_cnt_dic)
print(user_dic)
print(result)
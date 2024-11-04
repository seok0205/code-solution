'''
n개의 계약 조항이 있다. 약관의 종류에 따라 기간이 다르고, 기간이 다다르면 해당 계약은 파기가 된다.
주어진 사항은 오늘의 날짜(today), 약관 종류(terms), 계약을 시작한 날짜와 해당 계약의 약관 종류(privacies)이다.
privacies와 terms를 봤을 때, today의 날짜에 파기되어있어야하는 계약의 번호를 구하시오. 번호는 privacies[i]가 해당 계약일 때, i+1이 그계약의 번호다.
'''

today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

terms_dic = {}  # 약관 종류 dic
result = [] # 파기되어야하는 계약
today_year, today_month, today_day = map(int, today.split('.'))
today_total = (today_year * 28 * 12) + (today_month * 28) + today_day   # 오늘 날짜를 총 일수로 계산한 변수.

for i in terms: # terms_dic에 약관의 기간을 일수로 저장.
    t, t_month = i.split()
    terms_dic[t] = int(t_month) * 28

for i in range(len(privacies)):
    p_date, p_type = privacies[i].split()   # 날짜와 약관 종류로 분할.
    year, month, day = map(int, p_date.split('.'))  # 날짜를 일수로 계산하기 위해 '.'지우고 정수로 변환.
    total = (year * 28 * 12) + (month * 28) + day + terms_dic[p_type]   # 일수로 계산.
    if total <= today_total:    # 총 일수가 오늘 날짜의 총 일수보다 작으면 기간이 지난 것.
        result.append(i+1)  # result에 계약 번호 추가.

print(result)
'''
주차장 요금표(fees)와 입차, 출차 기록(records)이 주어질 때, 차량 번호가 작은 자동차 부터 청구할 차량별 주차 요금 계산.

입차 후 출차된 내역 없으면 23:59에 출차된 것으로 간주.
누적 주차 시간 기본 시간 이하면 기본 요금 청구.
누적 주차 시간이 기본 시간 초과 시, 기본 요금에 더해서 단위 시간마다 단위 요금 청구. 올림함.

제한 사항 :
len(fees) = 4
1 <= records <= 1,000

접근 :
1. 차량번호와 누적 시간을 측정할 딕셔너리 생성.
2. 시간 분 단위로. (시 * 60 + 분)형식, IN,OUT
3. 요금 정산
'''
import math

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

result = []
basic_time, basic_fee, per_min, plus_fee = fees # fees 구성.

car = {}    # (차 번호 : 0) 형태로 생성.
for i in records:
    i = i.split()
    car[i[1]] = 0

dic = {}    # (차량번호 : 입차 시간)
for i in records:
    i = i.split()
    temp = i[0].split(':')
    in_time = int(temp[0])*60 + int(temp[1])

    if i[2] == 'IN':
        dic[i[1]] = in_time

    elif i[2] == 'OUT': # car딕셔너리에 (차 번호 : 출차시간 - 입차시간) 형태로 저장.
        if i[1] in dic.keys():
            car[i[1]] += in_time - dic[i[1]]
            dic[i[1]] = -1

for key, value in dic.items():
    if value != -1: # 출차를 안한 경우. (0으로 하면 입차 시간이 00:00일 경우 오류 가능성.)
        car[key] = car[key] + (1439 - dic[key])

for key, value in car.items():
    if value <= basic_time: # 누적 시간이 기본 시간보다 아래면, 기본 요금만 받음.
        result.append((int(key), basic_fee))

    elif value > basic_time:    # 만약 기본 시간 초과 시, 단위 시간 경과 횟수에 따라 나누고 애매할 시에는 ceil()로 올림.
        tot_fee = basic_fee + math.ceil((value - basic_time)/per_min) * plus_fee
        result.append((int(key),tot_fee))

result.sort(key=lambda x : x[0])    # 차 번호 기준으로 오름차순 정렬.
result_1 = []
for key, money in result:
    result_1.append(money)

print(result_1)
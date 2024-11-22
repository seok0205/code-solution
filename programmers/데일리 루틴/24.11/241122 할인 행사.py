'''
원하는 제품을 나타내는 문자열 배열 want와 원하는 제품의 수량을 나타내는 number, 
마트에서 할인하는 제품을 나타내는 discount가 주어졌을 때, 원하는 제품을 모두 할인 받을 수 있는 회원 등록 날짜의 총 일수를 반환하라.

ex. 
want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
result = 3

제한 사항 :
1 <= len(want) = len(number) <= 10
1 <= number[i] <= 10
number[i]는 want[i]의 수량. sum(number) = 10.
10 <= len(discount) <= 100,000
want, discount의 원소는 소문자.
1 <= len(want[i]), len(discount[i]) <= 12

접근 :
1. 딕셔너리로 want, number을 각각 키와 밸류로 정하고 구성.
2. 총 행사 날이 14일이라 쳤을 때, 10일동안 회원이 구성되므로, 총 반복해야하는 경우의수는 n-9번.
3. 경우의 수 한번 탐색할 때마다, 딕셔너리를 복제해서, 초기화시켜줌.
4. discount의 품목들이 10일 연속으로, 원하는 개수 만큼 나오는 것이 목표이므로 if절 활용해서 조건 만족 시 계속 탐색, 조건 불만족시 해당 경우의수 중단.
5. 만약 그 경우의 수에서 모두 조건을 만족하면 result 값 1 증가.
'''

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

result = 0  # 결과값
dict_want = {}  # want(key), number(value)

for i in range(len(want)):  # 딕셔너리 구성.
    dict_want[want[i]] = number[i]

for i in range(len(discount) - 9):  # 경우의 수 모두 탐색.
    dict_cnt = dict_want.copy() # 조건 만족 판단할 딕셔너리 초기화
    for j in range(i, i+10):    # 조건 1. 10일 연속
        if discount[j] in dict_cnt and dict_cnt[discount[j]] != 0:  # 조건 2. want에 있어야 존재하고, 희망 구매 개수가 0이아닌 품목.
            dict_cnt[discount[j]] -= 1  # 조건 만족 시, dict_cnt의 해당 key의 value 1 감소.
        else:   # 만약 위 조건 2를 불만족 시 해당 경우의 수는 탐색 중지.
            break
    if sum(dict_cnt.values()) == 0: # 조건 1의 for문을 모두 수행한 결과 dict_cnt의 value값이 모두 사라져 0이 되면 모든 조건을 만족하는 경우의수.
        result += 1 # 결과값 1 증가.

print(result)

'''list로 푸는법

result = 0
list_want = []

for i in range(len(want)):
    for j in range(number[i]):
        list_want.append(want[i])
list_want.sort()

for i in range(len(discount)-9):
    list_cnt = discount[i:i+10]
    list_cnt.sort()
    if list_want == list_cnt:
        result += 1

print(result)
'''
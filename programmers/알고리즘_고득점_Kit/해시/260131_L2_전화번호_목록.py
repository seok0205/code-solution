'''
L2 전화번호 목록

문제 설명:
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 함.
119, 11 9552 4421의 경우 앞 번호가 뒷번호의 접두사임.
전화번호 담은 phone_book 배열이 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있다면 false, 그렇지 않으면 true를 return하는 문제.

제약:
phone_book의 길이는 1~1,000,000 이하임.
각 전번 길이는 1이상 20이하
같은 전화번호는 없음.
'''

def solution(phone_book):
    phone_dic = dict()
    for num in phone_book:
        phone_dic[num] = 0
    
    for num in phone_book:
        for i in range(1, len(num)):
            if num[:i] in phone_dic:
                return False
        
    return True
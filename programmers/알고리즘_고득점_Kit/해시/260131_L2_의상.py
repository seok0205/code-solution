'''
L2 의상

문제 설명:
매일 다른 옷을 조합하여 입으려고 함.
각 종류별로 최대 1가지 의상만 착용 가능. 같은 종류의 옷을 한번에 입을 순 없음.
착용한 의상 일부가 겹쳐도, 다른 의상이 겹치지 않거나 추가적으로 착용한 경우는 다른 방법으로 침.
하루에 최소 한개는 입음. 즉, 0종류를 입을 순 없음.

제약:
clothes의 각 행은 [의상이름, 의상종류]로 이루어져있음.
코니가 가진 의상 수는 1개 이상 30개 이하
같은 이름의 의상은 존재하지 않음.
clothes의 모든 원소는 문자열.
모든 문자열 길이는 1~20 자연수. 알파벳 소문자 혹은 _로만 이루어짐.
'''

def solution(clothes):
    clothes_dic = dict()
    
    for c_name, t_name in clothes:
        if t_name not in clothes_dic:
            clothes_dic[t_name] = 2
        else:
            clothes_dic[t_name] += 1
    
    result = 1
    for num in clothes_dic.values():
        result *= int(num)
        
    return result - 1
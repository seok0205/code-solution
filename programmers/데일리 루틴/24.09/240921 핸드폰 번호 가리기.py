def solution(phone_number):
    phone = phone_number[:-4]   #끝에서 4자리빼고 모두 *로 바꿈.
    number = ('*'*len(phone))
    
    return str(number + phone_number[-4:])  #바꾼 *문자열과 나머지 4자리 합쳐서 문자열로 출력.
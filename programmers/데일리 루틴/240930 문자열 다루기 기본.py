def solution(s):
    if len(s) == 4 or len(s) == 6:  #s의 길이가 4 혹은 6일 때
        for i in s: #s문자열 각 인덱스마다 반복. 
            if i >= '0' and i <= '9':   #0과 9 사이일때,
                continue    #계속 진행.
            else:   #0과 9사이가 아니라면, 숫자가 아니라면,
                return False    #False 도출.
        return True #모두 숫자여서 for문 진행이 완료되면 True 도출.
    else:   #s의 길이가 4나 6이 아니라면 False 도출.
        return False
    
def solution_A(s):  
	return s.isdigit() and len(s) in (4,6)
#isdigit은 숫자인지 확인해주는 함수. 길이가 4,6 둘 중 하나라는 조건 추가.
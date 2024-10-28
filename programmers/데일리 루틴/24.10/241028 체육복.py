# 학생 n명이 교실에 있다. 체육복을 도난 당한 사건이 생겼다.
# 잃어버린 학생이 lost배열에, 여벌의 옷을 가져온 학생이 reserve 배열에 번호가 저장되어있다.
# 체격크기 순서대로 번호가 저장되어있어 체육복은 본인 번호의 앞뒤번호의 학생에게만 빌려줄수 있다.
# 여벌의 옷을 가진 학생들이 잃어버린 학생들에게 체육복을 빌려줬을 때 체육복을 가질수 있는 최대 학생수를 구하는 문제.
# 단, 잃어버린학생도 여벌을 가져왔을 수 있다. 여벌은 단 한벌만 챙길 수 있다.

n = 5
lost = [2, 4]
reserve = [1, 3, 5]

def solution(n, lost, reserve):
    lost.sort() # 번호 정렬.
    reserve.sort()

    for i in reserve[:]:    # reserve배열, lost배열에 함께 있는 학생 색출 후 두 배열에서 삭제.
        if i in lost:   # 잃어버렸으나 여벌이 있으니 빌리지 않아도 됨.
            reserve.remove(i)
            lost.remove(i)

    for i in reserve:   # 잃어버리지 않은 reserve학생 중 lost에 있는 학생에게 빌려줌.
        if i-1 in lost: # 하지만 번호가 자기 앞이나 뒤여야 하는 조건.
            lost.remove(i-1)
        if i+1 in lost:
            lost.remove(i+1)

    answer = n - len(lost)  # 총 학생 수에서 lost에 남아있는 학생의 수를 뺌.
    return answer

print(solution(n, lost, reserve))
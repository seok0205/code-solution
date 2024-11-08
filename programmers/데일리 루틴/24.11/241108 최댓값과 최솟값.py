'''
문자열 s에 공백으로 구분된 숫자들이 저장되어 있음. str에 나타나는 숫자 중 최소값, 최대값을 찾아 
"(최소값) (최대값)"형태의 문자열을 반환하는 함수를 구성하는 문제.
'''

s = "-1 -2 -3 -4"

s = list(map(int, s.split()))   # 문자열을 숫자 상태에서의 비교를 위해 정수화, 리스트화 시킨다.

result= ''
min_num = s[0]  # 리스트의 첫 숫자가 최소, 최대값의 기준점.
max_num = s[0]

for i in s: # 모든 숫자 비교.
    if i <= min_num:    # i가 이전 최소값보다 작으면 i로 교체
        min_num = i
    elif i >= max_num:  # i가 이전 최대값보다 크면 i로 교체
        max_num = i

result = str(min_num) + ' ' + str(max_num)  # 다시 문자열로 변환.

print(result)
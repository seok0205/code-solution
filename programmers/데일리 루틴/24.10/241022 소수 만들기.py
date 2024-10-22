#주어진 숫자 배열중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하는 문제.
# ex) 1,2,7,6,4 배열을 받았을 때 소수의 개수는 4개. 4를 출력해야한다.

nums = [1, 2, 3, 4]

def solution(nums):
    answer = 0
    for i in range(len(nums)):  #첫번째 숫자 선택.
        for j in range(i+1, len(nums)): #두번째 숫자 선택.
            for k in range(j+1, len(nums)): #세번째 숫자 선택.
                a = nums[i] + nums[j] + nums[k] #세수의 합.
                rest = 0    #a가 소수인지 구할 때 쓰는 변수.
                for n in range(2, a):   #1과 a를 제외하고 나누어 떨어지지않으면 소수.
                    if a % n == 0:
                        rest += 1
                if rest == 0:   #나누어 떨어지는 수가 없으면 소수이므로
                    answer += 1 #1증가.
    return answer
'''
L1 폰켓몬

문제 설명:
폰켓몬의 종류가 nums 배열로 주어질 때, nums 길이인 N을 기준으로,
N//2 개만 폰켓몬을 선택한다고 함.
가장 많은 종류 i가지를 포함 시켰을 때, i를 구하는 문제

제약:
nums는 종류 번호 담긴 1차원 배열.
nums 길이는 1~10,000 자연수, 항상 짝수.
폰켓몬 종류 번호는 1~200,000 이하 자연수.
가장 많은 종류 폰켓몬 선택의 방법은 여러 가지라도, 선택 가능한 종류 개수 최댓값 하나만 출력.
'''

def solution(nums):
    N = len(nums)
    pocket_dic = dict()
    
    for num in nums:
        if num not in pocket_dic:
            pocket_dic[num] = 1
        else:
            pocket_dic[num] += 1
    
    if len(pocket_dic) < (N//2):
        answer = len(pocket_dic)
    else:
        answer = N//2

    return answer
'''
L2 주식가격

문제 설명:
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return하도록 함수 완성.

제약:
prices의 각 가격은 1 이상 10,000 이하 자연수
prices의 길이는 2 이상 100,000 이하.
'''

def solution(prices):
    chart = []
    result = [0] * len(prices)
    
    for i in range(len(prices)):
        while chart and prices[chart[-1][1]] > prices[i]:
            result[chart[-1][1]] = i - chart[-1][1]
            chart.pop()

        chart.append((prices[i], i))      
    
    while chart:
        idx = chart[-1][1]
        result[idx] = len(prices) - idx - 1
        chart.pop()
    return result
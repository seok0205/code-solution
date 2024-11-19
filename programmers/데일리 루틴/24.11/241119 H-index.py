'''
H-index는 과학자의 생산성, 영향력을 나타내는 지표.
논문 n편 중 h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-index.
과학자가 발표한 논문 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, H-index 반환하라.

제한 사항 :
1 <= (과학자가 발표한 논문의 수) <= 1000
0 <= (논문별 인용 횟수) <= 10000

접근 :
1. 먼저 주어진 citations 내림차순으로 정렬.
2. 인용 횟수와 논문 수가 같아지는 지점 인덱스에 위치한 값을 출력.
'''

citations = [3, 0, 6, 1, 5]

result = 0
citations.sort(reverse=True)

for i, citation in enumerate(citations):    # enumerate로 인덱스 번호(논문 개수)와 인용 당한 횟수 citation받음. i는 0부터니까 1을 더해주면 개수 증가와 같음.
    if citation >= i + 1:   # 논문 인용횟수가 개수와 같거나 커지기 시작할때가 h-index.
        result = i + 1

print(result)
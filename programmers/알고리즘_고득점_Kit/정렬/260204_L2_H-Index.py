'''
L2 H-Index

문제 설명:
H-Index는 과학자의 생산성과 영향력을 나타내는 지표. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 함. 위키백과1에 따르면, H-Index는 다음과 같이 구함

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성

제약:
과학자가 발표한 논문의 수는 1편 이상 1,000편 이하
논문별 인용 횟수는 0회 이상 10,000회 이하
'''

def solution(citations):
    citations.sort(reverse=True)
    result = 0
    idx = 0
    for citation in citations:
        if citation >= idx+1:
            result = idx+1
        idx += 1
    return result
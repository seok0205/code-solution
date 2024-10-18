#2016년은 2월이 29일인 윤년이다. 월과 일을 입력했을 때 해당 날의 요일을 구하는 문제.
#datetime를 임포트하면 쉽게 표현할 수 있지만 패키지를 안쓰고 하는게 의도인 것 같았다.

def solution(a, b):
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    i_month = a - 1 #입력받은 월. month 배열에서 해당 월의 일수는 인덱스 위치가 a-1이다.
    i_day = (sum(month[:i_month])+b)%7  #a의 전월까지 모두 일수를 더하고, b만큼 더해준뒤, 7로 나누면 몇번째 요일인지 알수가 있다.
    return day[i_day]   #요일 출력. 1월 1일이 금요일이므로, 인덱스가 1일때 금요일로 해두었다.

a, b = map(int, input().split())
print(solution(a, b))
#해당 기사의 공격력은 기사의 번호의 약수의 개수만큼 해당된다.
#하지만 Limit를 초과한 공격력은 power 공격력으로 고정되서 쓰여진다.
#무기를 제작하는 데에는 무기의 공격력만큼 철이 쓰인다. 
#기사가 number번까지 존재할 때, 모든 기사의 무기 제작에 쓰이는 철의 무게를 구하는 문제.

number = 10
limit = 3
power = 2

def solution(number, limit, power):
    iron = 0
    for i in range(number):
        atk = 0
        for j in range(1, int((i+1)**(1/2)+1)): # 가장 중요한 부분. 그냥 전체 범위로하면 시간 복잡도때문에 시간 초과에  걸림.
            if (i+1)%j == 0:    # 약수는 대칭성이 존재. 하나로 나눠지면 그에 대응하는 하나의 수도 약수.
                atk += 1
                if j**2 != (i+1):   # 하지만 제곱으로 약수도 나오는 경우도 존재. 그에 대비한 조건문.
                    atk += 1
        if atk > limit: #공격력이 limit 보다 높으면 철 무게에 power 대입.
            iron += power
        else:   #limit 넘지 않으면 원래 공격력만큼 철 무게에 더함.
            iron += atk
    return iron

print(solution(number, limit, power))

#약수 구하는 방법을 잘 숙지해야한다.
#제곱근을 활용한 for i in range(1, int(n**0.5)+1)을 기억하자. 약수 구하고 시간복잡도 줄이는데에 효율이 좋다.
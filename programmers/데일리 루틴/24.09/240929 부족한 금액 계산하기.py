def solution(price, money, count):
    sum_price = 0   #총합
    price_count = 0 #count에 따라 증가하는 회당 가격
    for i in range(1, count+1):
        price_count = price * i #탈때마다 원가격의 i배만큼 증가.
        sum_price += price_count    #총합도 탈 때마다 증가.
    if sum_price > money:   #계산된 총가격이 가진 돈보다 크면
        return sum_price - money    #총합과 보유한 돈의 차를 출력.
    else:   #돈이 부족하지 않으면 0 출력.
        return 0
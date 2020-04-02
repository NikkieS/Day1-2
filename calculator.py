price = 5.0
people = 120
before = 0

while True :
    #수입 = 티켓가격 * 관객수
    income = price * people

    #지출 = 고정비용(180) + (관객수 * 0.04)
    spending = 180 + (people * 0.04)

    #총수입 = 수입 - 지출
    profit = income - spending

    print('TOTAL :', profit , 'BEFORE :', before, 'Ticket :', price)

    if profit > before :
        before = profit

    else :
        break

    #변화
    price = price - 0.1
    people = people + 15
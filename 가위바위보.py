import random

def game() :
    user = int(input('0,1,2 중 하나를 고르세요 : '))
    com = random.randrange(0, 3)

    # 만일 컴이 사용자보다 작은 값이면 + 3
    if user > com:
        com = com + 3

    result = com - user

    if result == 2:
        result_str = 'USER'

    elif result == 1:
        result_str = 'COMPUTER'
    else:
        result_str = 'USER'

    return result_str

before = ' '
wincount = 0

while True :
    result = game()
    if result == before :
        wincount += 1
    else :
        wincount = 1
        before = result
    if wincount == 3 :
        print(result, 'won three times')
        break
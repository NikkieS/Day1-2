import random

before = ' '
user_win = 1
com_win = 1

while True :
    user = int(input('가위0, 바위1, 보2 중 하나를 고르세요 : '))
    com = random.randrange(0, 3)

    # 만일 컴이 사용자보다 작은 값이면 + 3
    if user > com:
        com = com + 3

    result = com - user
    print(result)

    if result == 2 :
        if before == result :
            user_win += 1
            com_win = 1
        before = result

    elif result == 1 :
        if before == result :
            user_win = 1
            com_win += 1
        before = result

    else :
        if before == 2 :
            user_win += 1
            com_win = 1
        before = result

    if user_win == 3 :
        print('user won three times')
        break
    elif com_win == 3 :
        print('computer won three times')
        break
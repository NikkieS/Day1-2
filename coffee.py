import random

value = random.randrange(0,4)
current = 0

while True :
    input('마음의 준비를 하시고 Enter')

    #print(current, value)

    if current == value :
        print('커피쏘기')
        break
    else :
        print('얻어먹기')

    current += 1


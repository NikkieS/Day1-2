min_num = 1
mid = 0
max_num = 100

while True :
    #print('Max', max_num, 'Min', min_num)
    mid = (min_num + max_num) // 2
    print('%d입니까?'%mid)
    user = input('높으면 H, 낮으면 L, 맞으면 C를 입력하세요.')

    if user == 'H' or user == 'h' :
        min_num = mid
        max_num = max_num

    elif user == 'L' or user == 'l' :
        min_num = min_num
        max_num = mid

    elif user == 'c' or user == 'C' :
        print('정답은 :', mid)
        break
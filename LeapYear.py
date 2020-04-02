year = int(input('년도를 입력하세요 : '))
'''
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) :
    print(str(year) + '년도는 윤년입니다.')
else :
    print(str(year) + '년도는 평년입니다.')
'''

if year % 400 == 0 :
    print('%d년도는 윤년입니다.'% year)
elif year % 100 == 0 :
    print('%d년도는 평년입니다.'% year)
elif year % 4 == 0 :
    print('%d년도는 윤년입니다.'% year)
else :
    print('%d년도는 평년입니다.'% year)
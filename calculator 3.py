GCD = 1 #Greatest Common Dividor 최대공약수
LCM = 1 #Least Common Multiple 최소공배수

num1 = int(input('숫자를 입력하세요 : '))
num2 = int(input('숫자를 입력하세요 : '))

loop_max = min(num1, num2) #나누는 값의 최대값
div = 2

num1_left = num1 #나머지값1
num2_left = num2 #나머지값2

if loop_max == 1 : #입력된 값 둘 중 하나가 1일 때
    GCD = 1
    LCM = num1 * num2

else : #입력된 값 둘 다 1이 아닐 때
    while True :
        if div > loop_max: #입력된 값중 작은 값보다 나누는 값이 커지면 빠져나온다
            break
        if num1_left%div == 0 and num2_left%div == 0 : #나누어 떨어질 때
            GCD = GCD * div # 최대공약수에 계속 곱함
            num1_left = num1_left / div #나머지값이 새로 나눠지는 값으로 치환됨
            num2_left = num2_left / div #나머지값이 새로 나눠지는 값으로 치환됨
        else : #나누어 떨어지지 않을 때
            div += 1

LCM = int(GCD * num1_left * num2_left)
print('최대공약수 :', GCD, '최소공배수 :', LCM)

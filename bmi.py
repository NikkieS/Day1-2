m = 1.7
kg = 50

bmi = kg / (m * m)

print(bmi)

if bmi < 18.5 :
    print('저체중')
elif bmi < 23 :
    print('정상체중')
elif bmi < 25 :
    print('과체중')
else :
    print('비만')
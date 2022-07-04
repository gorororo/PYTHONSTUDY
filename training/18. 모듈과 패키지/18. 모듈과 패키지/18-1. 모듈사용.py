import circleModule as cm

radius = int(input("반지름 입력 : "))

print('반지름 : ', radius)
print('원의 둘레 : ', round(cm.getCircumference(radius),2))
print('원의 넓이 : ', round(cm.getCircleArea(radius),2))

print('__name__:',cm.__name__)
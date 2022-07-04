PI = 3.14

# 원의 둘레
def getCircumference(radius):
    return 2*PI*radius

# 원의 넓이
def getCircleArea(radius):
    return PI*radius*radius

print('circleModule', PI)

if __name__ == "__main__":
    print('main_circleModule', PI) 
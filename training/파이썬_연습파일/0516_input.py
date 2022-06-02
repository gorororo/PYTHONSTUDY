# 0516_input.py

#a = input()
#print('입력받은 글자는',a)
#print(type(a))

#name = input('이름:')
#age = input('나이:')
#print(name,age)
#print('이름은' ,name,'이고 나이는',age, '입니다.')

#국어 , 영어 , 수학 , 점수를 받아서 총점 , 평균 구하기
kor=int(input('국어점수'))
eng=int(input('영어점수'))
math=int(input('수학점수'))
plus=kor+eng+math
mean=plus/3
print('총점:',plus)
print('평균:',mean)

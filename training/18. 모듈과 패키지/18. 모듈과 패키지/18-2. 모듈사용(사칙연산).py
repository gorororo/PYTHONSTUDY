import calModule as c

a, b = input('숫자 두개를 공백으로 구분하여 입력하세요 : ').strip().split()
a, b = int(a), int(b)

print(f'{a}+{b} = {c.add(a,b)}')
print(f'{a}-{b} = {c.sub(a,b)}')
print(f'{a}*{b} = {c.mul(a,b)}')
print(f'{a}/{b} = {c.div(a,b)}')

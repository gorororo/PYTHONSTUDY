def add(a, b): return a+b

def sub(a, b): return a-b

def mul(a, b): return a*b

def div(a, b):
    if b == 0:
        return 0
    return a / b

print('calModule 입니다.')

if __name__ == "__main__" :
    print('calModule')
    print('__name__:',__name__)
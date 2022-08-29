def my_fib_seq(n):
    a,b=0,1
    seq = [a,b]
    for i in range(n-2):
        a,b = b,a+b
        seq.append(b)
    return seq
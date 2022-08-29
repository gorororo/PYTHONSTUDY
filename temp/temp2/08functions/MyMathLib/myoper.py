def my_powers(number):
    return number,number**2,number**3

def my_sum(num_list):
    total = 0
    for num in num_list:
        total += num
    return total

def my_mean(num_list):
    s= my_sum(num_list)
    N=len(num_list)
    return s/N
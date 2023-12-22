

def a_prog(n):

    start_num = 1
    step = 2
    sum = n * (2 * start_num + (n - 1) * step) // 2
    if n < 0:
        raise AssertionError
    return sum


print(a_prog(5))



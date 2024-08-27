def test(*params):
    print(params)


test(1, 2, 'aaa', True)


def fact(n):
    a = 1
    for i in range(1, n+1):
        a = a * i
    print('Факториал числа n:',a)


fact(5)
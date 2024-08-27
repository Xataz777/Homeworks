def is_prime(func):
    def wrapper(a, b, c):
        r = func(a, b, c)
        if (r % 2 == 0 or r <= 1) and r != 2:
            print('Составное')
            return r
        elif r == 2:
            print('Простое')
            return r
        else:
            for i in range(3, int(r**0.5), 2):
                if r % i == 0:
                    print('Составное')
                    return r
        print('Простое')
        return r
    return wrapper

@is_prime
def sum_three(a, b, c):
    sum = a + b + c
    return sum

print(sum_three(0, 2, 0))
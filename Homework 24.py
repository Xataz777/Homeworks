def add_everything_up(a, b):
    try:
        c = a + b
    except TypeError:
        a = str(a)
        b = str(b)
        c = a + b
    return c


print(add_everything_up(4, 21))
print(add_everything_up('5', 45))
print(add_everything_up(2, 'fff'))
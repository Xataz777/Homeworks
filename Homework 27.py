def apply_all_func(int_list, *functions):
    results = {}
    for fun in functions:
        fun(int_list)
        results[fun.__name__] = fun(int_list)
    return results


def sum(a):
    res = 0
    for i in a:
        res += i
    return res


print((apply_all_func([2, 3, 17, 0], max, min, sum)))
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(3, 'string')
print_params()
print_params(c = False)

print_params(b = 25) # Работает
print_params(c = [1, 2, 3]) # Работает

values_list = ['stroka', True, 5]
values_dict = {'b':'stroka', 'c':2, 'a':True}
print_params(*values_list)
print_params(**values_dict)

values_list2 = [4, 'False']
# print_params(*values_list2, 2, 42)
# Не работает
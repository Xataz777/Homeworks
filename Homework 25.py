def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in range(len(numbers)):
        try:
            result = result + numbers[i]
        except TypeError:
            print('Некорректный тип данных для подсчёта суммы:', numbers[i])
            incorrect_data += 1
    r1 = (result, incorrect_data)
    return r1

def calculate_average(numbers):
    try:
        a = personal_sum(numbers)
        r2 = a[0] / (len(numbers) - a[1])
    except ZeroDivisionError:
        r2 = 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        r2 = None
    return r2


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
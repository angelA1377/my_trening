def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])

    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

# Пример использования
result = get_multiplied_digits(234)
print(result)  # Вывод: 24 (2 * (3 * 4))

# Создаём функцию print_params
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(b = 25)
print_params(c = [1,2,3])
# распаковка параметров
values_list = [54.32, 'Строка', [1, 2, 3]]
values_dict = {'a': 54.32, 'b': 'Строка', 'c': [1, 2, 3]}

print_params(*values_list)
print_params(**values_dict)
# Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
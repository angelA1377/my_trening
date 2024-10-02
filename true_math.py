# Создаем модуль true_math
from math import inf

# создаём фу-цию divide
def divide(first, second):
    if second == 0:
        return inf
    else:
        return first / second

# print(divide(49, 7))
# print(divide(15, 0))
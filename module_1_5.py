#2
immutable_var = 1, 2, True, 'яблоко'
immutable_var = tuple([1, 2, True, 'яблоко'])
print(type(immutable_var))
print(immutable_var)
print(immutable_var[3])

# 3
#immutable_var[0]=200
#кортеж не поддерживает обращение по элементам

#4
mutable_list=['красный','оранжевый', 'желтый','зеленый']
mutable_list[1]='orange'
print(mutable_list)

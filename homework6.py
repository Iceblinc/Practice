my_dict = {'Ноль': [0], "Один": [1], 'Два': [2]}
print(my_dict)
print(my_dict['Ноль'])
print(my_dict.get('Три', 'Такого ключа нет'))
my_dict.update({"Четыре": 4, "Пять": 5})
a = my_dict.pop('Ноль')
print(a)
print(my_dict)

my_set = {1, 1, 'Привет', 'Привет', True, True, (1, 2, 3), (1, 2, 3)}
print(my_set)
print(my_set.add(2))
print(my_set.add((1, 2, 4, 6)))
print(my_set.remove('Привет'))
print(my_set)
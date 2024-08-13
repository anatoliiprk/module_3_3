print('')
print('Задание "Распаковка"')
print('-----------')
print('')

def print_params (a = 1, b = 'Строка', c = True):
    print(a, b, c)

print_params()
print_params(2)
print_params(3.1, 'Cтрока_2')
print_params(False, 5.6, 'Cтрока_3')
print_params(b = 25)
print_params(c = [1, 2, 3])
print('-----------')
print('')

values_list = [4.5, False, 'Строка_4']
values_dict = {'a': True, 'b': 'Строка_5', 'c': [98, 46, 77]}

print_params(*values_list)
print_params(**values_dict)
print('-----------')
print('')

values_list2 = [3.14, 'Строка_6']
print_params(*values_list2, 42)
print('-----------')
print('Конец выполнения задания')
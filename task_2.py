# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна
# возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions

import fractions

x = input('Введите 1 дробь вида a/b: ')
y = input('Введите 2 дробь вида a/b: ')

x_f = x.split('/')
y_f = y.split('/')
res_1 = (int(y_f[0]) / int(y_f[1])) + (int(x_f[0]) / int(x_f[1]))
res_2 = (int(y_f[0]) / int(y_f[1])) * (int(x_f[0]) / int(x_f[1]))

f1 = fractions.Fraction(int(x_f[0]), int(x_f[1]))
f2 = fractions.Fraction(int(y_f[0]), int(y_f[1]))

print(f'{res_1 = }\n{res_2 = }')
print(f'сумма = {f1 + f2}\nпроизведение = {f1 * f2}')


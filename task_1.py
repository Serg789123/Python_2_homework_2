# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = int(input('Введите целое число: '))
HEX = 16
res = ''
hexadecimal_digits = '0123456789abcdef'

print(hex(num))

while num > 0:
    ordinal = num % HEX
    n = hexadecimal_digits[ordinal]
    res = n + res
    num //= HEX

print(res)








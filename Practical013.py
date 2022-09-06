# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# - 0,56 -> 11

num = input('Введите вещественное число: ')
element = 0
result = 0

for i in range (0, len(num)):
    element = num[i]
    if element == '.':
        continue
    result += int(element)

print(result)

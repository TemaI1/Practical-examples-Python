# Задайте два числа. Напишите программу, 
# которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# Ответ записать в файл.

a = int(input('Введите a: '))
b = int(input('Введите b: '))
count = a * b

while(a != b):
    if a > b:
        a = a - b
    else:
        b = b - a
print(count / a)

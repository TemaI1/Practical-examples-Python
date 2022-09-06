# Задайте список из k чисел последовательности 
# (1 + 1\k)^k и выведите на экран их сумму.

num = int(input('Введите число: '))
result = 0

for i in range(1, num + 1):
    result += ((1 + 1 / i)**i)
print(result)

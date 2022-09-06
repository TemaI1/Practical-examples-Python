# Напишите программу, которая принимает на вход число N и 
# выдаёт последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81

# num = int(input('Введите число: '))
# result = [1] * num

# for i in range(1, num):
#     result[i] = result[i-1] * -3
# print(result)



num = int(input('Введите число: '))
result = [1] * num
i = 1

while i < num:
    result[i] = result[i - 1] * -3
    i += 1
print(result)

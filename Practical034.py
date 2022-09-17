# Дан список чисел. Создайте список, в который попадают числа, описываемые 
# возрастающую последовательность. Порядок элементов менять нельзя. 
# *Пример:* 
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7] и т.д.

# numbers = [1, 5, 2, 3, 4, 6, 1, 7]
# list = []
# num = numbers[0]
# list.append(num)

# for i in range(len(numbers) - 1):
#     if num < numbers[i + 1]:
#         num = numbers[i + 1]
#         list.append(num)

# print(list)



my_list = [1, 5, 2, 3, 4, 6, 1, 7]
count = 0 
new_list = ([my_list[i] for i in range(1,len(my_list)) if my_list[i] >= max(my_list[0:i])])
new_list.insert(0, my_list[0])
print(new_list)

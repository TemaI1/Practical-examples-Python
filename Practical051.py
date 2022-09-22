# Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности.
# *Пример:* 
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

incoming_list = [1, 2, 3, 5, 1, 5, 3, 10]
outcoming_list = [i for i in incoming_list if incoming_list.count(i) == 1]
print(outcoming_list)

incoming_list2 = [1, 2, 3, 5, 1, 5, 3, 10]
outcoming_list2 = list(filter(lambda x: incoming_list2.count(x) == 1, incoming_list2))
print(outcoming_list)

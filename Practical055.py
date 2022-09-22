# Функция map() в Python

old_list = ['1', '2', '3', '4', '5', '6', '7']
new_list = []
for item in old_list:
    new_list.append(int(item))
print(new_list)

old_list2 = ['1', '2', '3', '4', '5', '6', '7']
new_list2 = list(map(int, old_list2))
print(new_list2)
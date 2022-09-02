# Найти максимальный элемент в листе и его значение

my_list = [3, 13, 9, 7, 5]
maxx = my_list[0]
maxx_i = 0
for i in range(1, len(my_list)):
    if my_list[i] > maxx:
        maxx = my_list[i]
        maxx_i = i

print(maxx, maxx_i)


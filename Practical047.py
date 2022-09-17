# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# import random

# Первый ход определяется жеребьёвкой:
# player = random.randint(1, 2)
# print(player)
# if player == 2:
#     variable_player = candies_second
#     candies_second = candies_first
#     candies_first = variable_player

# Добавьте игру против бота:
# candies_second = random.randint(1, 28)

candy = 2021
max_candy = 28
candies_first = int(input('Сколько конфет возьмет первый игрок: '))
candies_second = int(input('Сколько конфет возьмет второй игрок: '))
result_first = 0
result_second = 0

while result_first <= candy and result_second <= candy:
    if candies_first <= max_candy:
        result_first = candies_first + result_second
    else:
        print(f'Первый игрок взяли слишком много конфет, разрешается не более {max_candy} конфет')
        candies_first = int(input('Ещё раз, сколько конфет возьмет первый игрок: '))
    if result_first >= candy:
        break
    if candies_second <= max_candy:
        result_second = candies_second + result_first
    else:
        print(f'Второй игрок взял слишком много конфет, разрешается не более {max_candy} конфет')
        candies_second = int(input('Ещё раз, сколько конфет возьмет второй игрок: '))
print(f'Конфет первого игрока: {result_first}')
print(f'Конфет второго игрока: {result_second}')

if result_first >= candy:
    print(f'Победил первый игрок')
else:
    print(f'Победил второй игрок')

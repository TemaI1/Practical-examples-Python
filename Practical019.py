# Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.
# ['65h34q', 'sdg634d', '147jnbv']
# "7"



# n_list = ['ttt', 'rrr1', 'eee2']

# n = int(input('Введите число : '))
# n1 = str(n)

# for i in range(len(n_list)):
#     str1 = n_list[i]
#     a = str1.find(n1)
#     #print(a)
#     if (a > 0):
#         print(f'В ячейке {i+1} присутствует число "{n1}"')




# listt = ["65h34q", "sdg634d", "147jnbv"]

# result = [i for i in listt if '147' in i]
# print(result)
# if len(result) > 0:
#     print(True)
# else:
#     print(False)



# n = 'h'  
# mylist = ['jh', 'sdhfogf', 'kjahsd', '24', 'dpo', '7']
# def find_number(n, lst):
#     res = []
#     for i in lst:
#         if n in i:
#             res.append(i)
#     return res
# print(find_number(n, mylist))




myList = ['65h734q', 'sdg634d', '147jnbv']
n = '7'
for i in myList:
    if i.find(n) >= 0:
        print(i)

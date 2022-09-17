# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие 
# A[i] - 1 = A[i-1]. Найдите это число.

string = [1, 2, 4, 4, 5]
string = list(map(int, string))

for i in range(1, len(string)):
    if string[i] - 1 != string[i - 1]:
        print(f'Missed: {string[i] - 1}')
        break
else:
    print('Goog')

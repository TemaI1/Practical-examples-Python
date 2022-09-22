
in_list = [1, 2, 1, 3, 3, 5, 6, 7, 9, 6]

result = [item for item in in_list if in_list.count(item) == 1]
print(result)

result2 = tuple(filter(lambda x: x > 3, in_list))
print(result2)

result3 = tuple(filter(lambda x: in_list.count(x) == 1, in_list))
print(result3)

input_list = ['wer', '2', '1', 'dfgh', 'gh', '5', '6', '7', 'er', '6']
result4 = list(map(lambda x: int(x) if x.isdigit() else x, input_list))
print(result4)


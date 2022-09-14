# Вычислить число c заданной точностью d
# Пример: при $d = 0.001, π = 3.141

import math

number = '0.001'
pi = str(math.pi)
result = str()
count = 0

for i in number:
    result += pi[count:count + 1]
    count += 1
print(result)

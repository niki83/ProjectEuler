# 1)
# Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
#
# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
#
#
# num_list = [num for num in range(1001) if num % 3 == 0 or num % 5 == 0]
# rezult = sum(num_list)
# print(rezult)

#  2)
# Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.



# s, a, b = 0, 1, 2
# while b < 4000000:
#     if b % 2 == 0:
#         s += b
#     a, b = b, a + b
#
# print(s)

import this
import antigravity


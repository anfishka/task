# В 3х мерном массиве (заполнить случайными 1-10) найти количество чисел в диапазоне 1-4
import random

arr = []

count = 0

for i in range(3):
    arr_temp = []
    for j in range(10):
        num = random.randint(1, 10)
        arr_temp.append(num)
        if 1 <= num <= 4:
            count += 1
    arr.append(arr_temp)
print(arr)
print("Amount of nums from 1 to 4:", count)

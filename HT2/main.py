import math
import random

import numpy as np


# Циклы
# 1
# while True:
#     a = int(input())
#     b = int(input())
#     print("Sum:", a+b)
#

# 2
# n = 5
# index = 1
# for i in range(n):
#     s = ""
#     for j in range(n):
#         if j % 2 != i % 2:
#             s += str(index)
#             index += 1
#         else:
#             s += '*'
#         s += "\t"
#     print(s)


# 3
# print("Загадайте число в интервале")
# low = int(input("Введите нижнюю границу: "))
# high = int(input("Введите верхнюю границу: "))
#
# attempts = 0
# while low <= high:
#     mid = (low + high) // 2
#     attempts += 1
#
#     print(f"Число равно {mid}?")
#     answer = input("Введите '1', если верно, '>', если ваше число больше, и '<', если ваше число меньше: ")
#
#     if answer == '1':
#         print(f"Ура! Я угадал ваше число {mid} за {attempts} попыток")
#         break
#     elif answer == '>':
#         low = mid + 1
#     elif answer == '<':
#         high = mid - 1
#     else:
#         print("Некорректный ввод")

# 4
# biggest = 0
# while True:
#     s = int(input())
#     if s == 0:
#         break
#     if biggest < s:
#         biggest = s
#
# print(biggest)

# 5
# for i in range(1, 10):
#     s = ""
#     for j in range(1, 10):
#         s += f'{j} * {i} = {i * j}\t\t'
#     print(s)

# Списки

# 1
# data = [23, 1, 45, 345, 78, 34, 12, 456, 89, 5, 67, 43, 56, 34, 12, 0, 123, 1234, 45, 6436, 346, 41, 24]
#
# print(min(data), max(data), np.median(data))

# 2
# max_value = 100
# count = 20
#
# data = np.random.randint(0, max_value, count)
# print("Список:", data)
#
# bins = 10
#
# min_val, max_val = min(data), max(data)
# bin_size = (max_val - min_val) / bins
# histogram = [0] * bins
#
# for value in data:
#     bin_index = int((value - min_val) / bin_size)
#     if bin_index == bins:
#         bin_index -= 1
#     histogram[bin_index] += 1
#
# probabilities = [count / len(data) for count in histogram]
#
# print("Количество значений в бинах: ", histogram)
# print("Вероятности: ", probabilities)

# 3

# N = int(input())
#
# vector1 = np.random.randint(0, 101, N)
# vector2 = np.random.randint(0, 101, N)
# print("Вектор 1:", vector1)
# print("Вектор 2:", vector2)
#
# sum_vector = vector1 + vector2
# mul_vector = vector1 * vector2
#
# print("Суммирование:", sum_vector)
# print("Перемножение:", mul_vector)
#
# norm_vector1 = np.linalg.norm(vector1)
# norm_vector2 = np.linalg.norm(vector2)
#
# scalar = 2
# if norm_vector1 > norm_vector2:
#     print("Умножение на скаляр:", vector1 * scalar)
# else:
#     print("Умножение на скаляр:", vector2 * scalar)

# 4

# count = 5
# max_value = 20
# matrix = []
# print("Матрица:")
# for i in range(count):
#     t = np.random.randint(0, max_value, count)
#     print(t)
#     matrix.append(t)
#
# print("\n")
# vector = np.random.randint(0, max_value, count)
# print("Вектор:", vector, "\n")
#
# result = []
# for row in matrix:
#     row_result = 0
#     for i in range(len(vector)):
#         row_result += row[i] * vector[i]
#     result.append(int(row_result))
# print("Результат:", result)

# 5

# count = 10
# data = np.random.randint(-100, 101, count)
# print(data)
#
# for i in range(count):
#     if data[i] > 0:
#         continue
#     sr = 0
#
#     for j in range(i, count, 1):
#         if data[j] < 0:
#             continue
#         else:
#             sr = data[j]
#             break
#
#     for k in range(i, 0, -1):
#         if data[k] < 0:
#             continue
#         else:
#             sr = (sr + data[k])/2
#             break
#     data[i] = sr
#
# print(data)

# 6
# data = [1, 4, 6, 8, 10, 12, 14, 16, 18]
# kernel = [1, 0, 1]
# kernel_len = len(kernel)
# result = []
#
# for i in range(len(data) - kernel_len + 1):
#     window = data[i:(i + kernel_len)]
#
#     conv_value = 0
#     for j in range(kernel_len):
#         conv_value += window[j] * kernel[j]
#     result.append(conv_value)
#
# print(result)



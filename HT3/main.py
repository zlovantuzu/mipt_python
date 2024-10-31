import math
import random

import numpy as np


# функции
# 1

# def mult_table():
#     for i in range(1, 10):
#         s = ""
#         for j in range(1, 10):
#             s += f'{j} * {i} = {i * j}\t\t'
#         print(s)
#
# def sum_table():
#     for i in range(1, 10):
#         s = ""
#         for j in range(1, 10):
#             s += f'{j} + {i} = {i + j}\t\t'
#         print(s)
#
# def sub_table():
#     for i in range(1, 10):
#         s = ""
#         for j in range(1, 10):
#             s += f'{j} - {i} = {i - j}\t\t'
#         print(s)
#
# def div_table():
#     for i in range(1, 10):
#         s = ""
#         for j in range(1, 10):
#             s += f'{j} / {i}  {i / j}\t\t'
#         print(s)
#
#
# type = int(input("Введите типа таблицы для вывода: \nУмножения - 1\nСложения - 2\nВычитания - 3\nДеления - 4\n"))
#
# match type:
#     case 1:
#         mult_table()
#     case 2:
#         sum_table()
#     case 3:
#         sub_table()
#     case 4:
#         div_table()


# 2

# def create_vector(n):
#     vector = []
#     for i in range(n):
#         vector.append(random.random())
#     return vector
#
#
# # print(create_vector(10))
#
# def create_matrix(n, m):
#     matrix = []
#     for i in range(m):
#         matrix.append(create_vector(n))
#     return matrix
#
#
# # print(create_matrix(5,5))
#
# def mult_matrix_vector(matrix, vector):
#     result = []
#     for row in matrix:
#         row_result = 0
#         for i in range(len(vector)):
#             row_result += row[i] * vector[i]
#         result.append(row_result)
#     return result
#
#
# def print_matrix(matrix):
#     for row in matrix:
#         s = ""
#         for v in row:
#             s += str(v) + "\t"
#         print(s)
#
#
# def print_vector(vector):
#     s = ""
#     for v in vector:
#        s += str(v) + "\t"
#     print(s)
#
# def sum_matrix(matrix):
#     s = 0
#     for row in matrix:
#         for v in row:
#             s += v
#     return s
#
# def sum_diag_matrix(matrix):
#     n = len(matrix)
#     main_diagonal_sum = 0
#     secondary_diagonal_sum = 0
#
#     for i in range(n):
#         main_diagonal_sum += matrix[i][i]
#         secondary_diagonal_sum += matrix[i][n - i - 1]
#
#     total_sum = main_diagonal_sum + secondary_diagonal_sum
#     return total_sum
#
#
# def fold_2d(matrix, kernel):
#     m = len(matrix)
#     n = len(matrix[0])
#     k = len(kernel)
#     l = len(kernel[0])
#
#     result = create_matrix(m - k + 1, n - l + 1)
#
#     for i in range(m - k + 1):
#         for j in range(n - l + 1):
#             m = []
#             for ii in range(i, i+k):
#                 sub_m = []
#                 for jj in range(j, j + l):
#                     sub_m.append(matrix[ii][jj])
#                 m.append(sub_m)
#
#             m_mult_k = []
#             for ii in range(len(m)):
#                 sub_m = []
#                 for jj in range(len(m[ii])):
#                     sub_m.append(m[ii][jj] + kernel[ii][jj])
#                 m_mult_k.append(sub_m)
#
#             result[i][j] = sum_matrix(m_mult_k)
#
#     return result
#
#
# vector = create_vector(3)
# matrix = create_matrix(3, 3)
# print("Результат:", mult_matrix_vector(matrix, vector))
#
# print_vector(vector)
# print("#############")
#
# print_matrix(matrix)
# print("#############")
#
# print(sum_diag_matrix(matrix))
# print("#############")
#
# matrix2 = create_matrix(4, 4)
# kernel = create_matrix(2, 2)
# print_matrix(fold_2d(matrix2, kernel))



#3

# def create_empty_vector(n):
#     vector = []
#     for i in range(n):
#         vector.append(0)
#     return vector
#
#
# def create_empty_matrix(n, m):
#     matrix = []
#     for i in range(m):
#         matrix.append(create_empty_vector(n))
#     return matrix
#
#
# def sum_matrix(matrix):
#     s = 0
#     for row in matrix:
#         for v in row:
#             s += v
#     return s
#
#
# def fold_2d(matrix, kernel):
#     m = len(matrix)
#     n = len(matrix[0])
#     k = len(kernel)
#     l = len(kernel[0])
#
#     result = create_empty_matrix(m - k + 1, n - l + 1)
#
#     for i in range(m - k + 1):
#         for j in range(n - l + 1):
#             m = []
#             for ii in range(i, i+k):
#                 sub_m = []
#                 for jj in range(j, j + l):
#                     sub_m.append(matrix[ii][jj])
#                 m.append(sub_m)
#
#             m_mult_k = []
#             for ii in range(len(m)):
#                 sub_m = []
#                 for jj in range(len(m[ii])):
#                     sub_m.append(m[ii][jj] + kernel[ii][jj])
#                 m_mult_k.append(sub_m)
#
#             result[i][j] = sum_matrix(m_mult_k)
#
#     return result
#
#
# def filter_image(image_2d):
#     kernel = [
#         [1, 0],
#         [0, 1],
#     ]
#     return fold_2d(image_2d, kernel)
#
#
# def multichannel_decorator(func):
#     def wrapper(image_3d):
#         filtered_channels = []
#         for i in range(3):
#             image_2d = []
#             for row in image_3d:
#                 r = []
#                 for v in row:
#                     r.append(v[i])
#                 image_2d.append(r)
#             filtered_channel = filter_image(image_2d)
#             filtered_channels.append(filtered_channel)
#         return func(image_3d)
#     return wrapper
#
#
# @multichannel_decorator
# def image_filter(image_3d):
#     return image_3d
#
# #
# image = [
#         [[5,1,4], [4,6,7], [1,4,9]],
#         [[2,5,2], [1,7,1], [3,9,3]],
#         [[4,1,5], [7,6,4], [9,4,1]],
#     ] #3d image
#
# print(image_filter(image))


#4

# def convert_color(color_vector):
#     color_model = color_vector[3]
#
#     if color_model == 0:
#         # из RGB в YIQ
#         R, G, B, _ = color_vector
#         Y = 0.299 * R + 0.587 * G + 0.114 * B
#         I = 0.5959 * R - 0.2746 * G - 0.3213 * B
#         Q = 0.2115 * R - 0.5227 * G + 0.3112 * B
#         return [Y, I, Q, 1]
#     elif color_model == 1:
#         # из YIQ в RGB
#         Y, I, Q, _ = color_vector
#         R = Y + 0.956 * I + 0.621 * Q
#         G = Y - 0.272 * I - 0.647 * Q
#         B = Y - 1.106 * I + 1.703 * Q
#
#         # R = 0 if R < 0 else (1 if R > 1 else R)
#         # G = 0 if G < 0 else (1 if G > 1 else G)
#         # B = 0 if B < 0 else (1 if B > 1 else B)
#         return [R, G, B, 0]
#
#
# rgb_vector = [0.5, 0.9, 0.1, 0]
# yiq_vector = convert_color(rgb_vector)
# print("RGB -> YIQ:" + str(yiq_vector))
#
# rgb2_vector = convert_color(yiq_vector)
# print("YIQ -> RGB:" + str(rgb2_vector))


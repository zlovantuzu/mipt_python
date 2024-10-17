import matrix_tools
import time


# vector = matrix_tools.create_empty_vector(5)
# print(vector)


# matrix = matrix_tools.create_empty_matrix(5, 5)
# print(matrix)


# matrix = matrix_tools.sum_matrix([[1,1,1],[2,2,2],[5,5,5]])
# print(matrix)


# m1 = [[1,1,1],[2,2,2],[5,5,5]]
# m2 = [[3,5,3],[9,9,2],[5,2,1]]
# matrix = matrix_tools.matrix_multiply(m1,m2)
# print(matrix)

# m1 = [[1,1,1],[2,2,2],[5,5,5]]
# v1 = [3,2,1]
# matrix = matrix_tools.mult_matrix_vector(m1,v1)
# print(matrix)




# тестовый код на замер времени выполнения и записть данных в файл
times = []
for i in range(5, 200):
    start_time = time.time()

    matrix = matrix_tools.create_empty_matrix(i, i)

    k = matrix_tools.create_empty_matrix(i-4, i-4)
    matrix_tools.fold_2d(matrix, k)

    end_time = time.time()
    ex_time = end_time - start_time
    times.append(ex_time)

matrix_tools.write_to_file("test_file.txt", times)

# чтобы ускорить этот код не надо делать большое количество for в for (а вообще этот код ничего не делает полезднного, так что его надо просто убрать)

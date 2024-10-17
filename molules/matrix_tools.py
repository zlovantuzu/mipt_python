def create_empty_vector(n):
    vector = []
    for i in range(n):
        vector.append(0)
    return vector


def create_empty_matrix(n, m):
    matrix = []
    for i in range(m):
        matrix.append(create_empty_vector(n))
    return matrix


def sum_matrix(matrix):
    s = 0
    for row in matrix:
        for v in row:
            s += v
    return s


def matrix_multiply(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        return None

    result = create_empty_matrix(rows_A, cols_B)

    for i in range(rows_A):
        for j in range(cols_B):
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(cols_A))

    return result


def mult_matrix_vector(matrix, vector):
    result = []
    for row in matrix:
        row_result = 0
        for i in range(len(vector)):
            row_result += row[i] * vector[i]
        result.append(row_result)
    return result


def matrix_trace(A):
    rows_A = len(A)
    cols_A = len(A[0])

    if rows_A != cols_A:
        return None

    trace = sum(A[i][i] for i in range(rows_A))

    return trace


def dot_product(v1, v2):
    if len(v1) != len(v2):
        return None

    return sum(v1[i] * v2[i] for i in range(len(v1)))


def calculate_histogram(vector, bins):
    min_val, max_val = min(vector), max(vector)
    bin_size = (max_val - min_val) / bins
    histogram = [0] * bins

    for value in vector:
        bin_index = int((value - min_val) / bin_size)
        if bin_index == bins:
            bin_index -= 1
        histogram[bin_index] += 1

    return histogram


def fold_2d(matrix, kernel):
    m = len(matrix)
    n = len(matrix[0])
    k = len(kernel)
    l = len(kernel[0])

    result = create_empty_matrix(m - k + 1, n - l + 1)

    for i in range(m - k + 1):
        for j in range(n - l + 1):
            m = []
            for ii in range(i, i+k):
                sub_m = []
                for jj in range(j, j + l):
                    sub_m.append(matrix[ii][jj])
                m.append(sub_m)

            m_mult_k = []
            for ii in range(len(m)):
                sub_m = []
                for jj in range(len(m[ii])):
                    sub_m.append(m[ii][jj] + kernel[ii][jj])
                m_mult_k.append(sub_m)

            result[i][j] = sum_matrix(m_mult_k)

    return result


def write_to_file(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(f"{item}\n")


def read_from_file(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            data.append(float(line.strip()))
    return data

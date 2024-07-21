def get_matrix(n, m, value):
    matrix = []

    for i in range(n):
        matrix_1 = []

        for j in range(m):
            matrix_1.append(value)

        matrix.append(matrix_1)
    return matrix

result = get_matrix(2, 2, 10)
result_1 = get_matrix(3, 5, 42)
result_2 = get_matrix(4, 2, 13)

print(result)
print(result_1)
print(result_2)

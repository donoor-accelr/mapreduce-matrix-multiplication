A_matrix_rows = 1000
A_matrix_columns = 500

B_matrix_rows = 500
B_matrix_columns = 1000


with open('ab_matrix_data_1000_500_500_1000.txt', 'w') as f:
    for i in range(1, A_matrix_rows + 1):
        for j in range(1, A_matrix_columns + 1):
            f.write('A {} {} {}\n'.format(i, j, i * j))

    for i in range(1, B_matrix_rows + 1):
        for j in range(1, B_matrix_columns + 1):
            f.write('B {} {} {}\n'.format(i, j, i * j))
f.close()
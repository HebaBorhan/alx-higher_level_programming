#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0 or len(matrix [0]) == 0:
        print("")

    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j != len(matrix[i]) - 1:
                    print("{}".format(matrix[i][j]), end=' ')
                else:
                    print("{}".format(matrix[i][j]), end='')
            print("")

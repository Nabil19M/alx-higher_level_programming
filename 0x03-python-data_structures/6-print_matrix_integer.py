#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print("{}".format(matrix[i][j]), end=' ')
            print()

import math
import numpy as np

def print_matrix(array2D):
    print('\n')
    for _list in array2D:
        for j in _list:
            print('{}'.format(j), end='\t')
        print('\n')
    


def min_mat_mul_count(mul_array):
    length = len(mul_array) - 1
    matrix = []
    mul_order = []
    for _ in range(length):
        matrix.append([0] * length)
        mul_order.append([0] * length)

    offset = 1
    for i in range(length - 1, 0, -1):
        for j in range(0, i):
            start = j
            end = j + offset
            matrix[start][end] = math.inf
            for k in range(start, end):
                current = matrix[start][k] + matrix[k + 1][end] + \
                    (mul_array[start] * mul_array[k + 1] * mul_array[end + 1])

                if current < matrix[start][end]:
                    matrix[start][end] = current
                    mul_order[start][end] = k

        print(np.matrix(matrix))
        print('\n')
        print(np.matrix(mul_order))
        
        print('\u2500' * 30)
        offset += 1

    return matrix[0][length - 1]


if __name__ == "__main__":
    mats = [13, 5, 89, 3, 34]
    result = min_mat_mul_count(mats)
    print('Minimum number of multiplications : {}'.format(result))

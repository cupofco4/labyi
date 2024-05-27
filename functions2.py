from math import sqrt, sin, cos, log


def generate_matrix(n, m):
    matrix = []
    
    for i in range(n):
        matrix.append([])
        for j in range(m):
            sin_i = sin(i)
            cos_j = cos(j)
            numerator = (i - 7)
            denominator = (j + 4)
            
            # Проверяем, чтобы избежать деления на ноль и отрицательного аргумента для логарифма
            if denominator != 0 and (abs(numerator / denominator) - 9) > 0:
                log_value = log(abs(numerator / denominator) - 9)
            else:
                log_value = 0 
            
            aij = (sin_i ** 3 - cos_j) ** 3 + 3.1 * log_value
            matrix[i].append(round(aij, 2))
    return matrix

def max_col_square():
    matrix = generate_matrix(6, 8)
    max_nums = []
    for i in range(len(matrix[0])):
        max_num = matrix[0][i] ** 2
        for j in range(1, len(matrix)):
            square_num = matrix[j][i] ** 2
            if square_num > max_num:
                max_num = square_num
        max_nums.append(round(max_num, 2))
    return str(max_nums) + '\nЗначение функции: ' + str(function_G(max_nums))


def function_G(max_nums: list):
    sum_of_vector = 0
    
    for i in range(len(max_nums)):
        sum_of_vector += max_nums[i] ** 3 + 30
    
    return sqrt(abs(sum_of_vector))

print(max_col_square())
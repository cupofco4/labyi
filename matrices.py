def absolute_sum_of_elements(lst: list):
    sum_value = 0
    for num in lst:
        sum_value += num
        
    return abs(sum_value)

def check_matrix1(matrix, num):
    nums_of_strings = []
    for i in range(len(matrix)):
        if absolute_sum_of_elements(matrix[i]) > num:
            nums_of_strings.append(i)
    
    if len(nums_of_strings) == 0:
        return 'Нет строк, удовлетворяющих условию!'
    return 'Количество строк: ' + str(len(nums_of_strings)) + '\nНомера строк: ' + str(nums_of_strings)

# ==================================================
def check_condition(lst, T):
    result = None
    start_index = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i == j:
                continue
            if abs(lst[i] - lst[j]) > T:
                result = sum(lst)
                break
        if result != None:
            break
        start_index += 1
    return result
            

# Вариант 1: Использование цикла с условием выхода
def variant_1(arr, T):
    for i in range(len(arr)):
        # Если рассмотрен вес двумерный массив
        if i == len(arr) - 1:
            print("Рассмотрен весь двумерный массив")
        # Проверяем условие досрочного выхода из цикла
        if check_condition(arr[i], T):
            # Выводим сумму элементов строки
            print("Сумма элементов строки", i, ":", sum(arr[i]))
            break

# Вариант 2: Использование цикла с условием выхода и досрочного завершения
def variant_2(arr, T):
    for i in range(len(arr)):
        # Если рассмотрен вес двумерный массив
        if i == len(arr) - 1:
            print("Рассмотрен весь двумерный массив")
        # Проверяем условие досрочного выхода из цикла
        if check_condition(arr[i], T):
            # Выводим сумму элементов строки
            print("Сумма элементов строки", i, ":", sum(arr[i]))
            return

# Вариант 3: Использование цикла с условием выхода и принудительного завершения
def variant_3(arr, T):
    for i in range(len(arr)):
        # Если рассмотрен вес двумерный массив
        if i == len(arr) - 1:
            print("Рассмотрен весь двумерный массив")
        # Проверяем условие досрочного выхода из цикла
        if check_condition(arr[i], T):
            # Выводим сумму элементов строки
            print("Сумма элементов строки", i, ":", sum(arr[i]))
            break
    return 

# ===============================================
def increase_column(matrix, index, C):
    for i in range(len(matrix[index])):
        matrix[i][index] += C[i]
    return matrix

def modify_matrix(matrix, C):
    sum_main_diagonal = 0
    for i in range(len(matrix)):
        sum_main_diagonal += matrix[i][i]
        if matrix[i][i] == 0:
            matrix = increase_column(matrix, i, C)
    
    # Вывод новой матрицы
    for row in matrix:
        for col in row:
            print(col, end=' ')
        print()
    return "Сумма главной диагонали - " + str(sum_main_diagonal)

if __name__ == '__main__':
    C = [1, 2, 3] 
    matrix = [[1, 0, 3],
              [0, 1, 4],
              [5, 6, 0]] 
    print(modify_matrix(matrix, C))
    # # Ни на одном фрагменте
    # variant_1([
    #     [3, 4, 5],
    #     [5, 2, 6],
    #     [1, 2, 3],
    #     [30, 34, 1],
    #     [5, 15, 59],
    #     [24, 54, 30],
    #     [24, 24, 30]], 550) 
    # print()
    # # На последнем фрагменте
    # variant_2([
    #     [3, 4, 5],
    #     [5, 2, 6],
    #     [1, 2, 3],
    #     [30, 34, 1],
    #     [5, 15, 59],
    #     [24, 54, 30],
    #     [24, 2433, 30]], 550) 
    
    # print()  
    # # Все кроме последнего
    # variant_3([
    #     [3444, 4, 5],
    #     [5, 2444, 6],
    #     [1, 2444, 3],
    #     [4430, 34, 1],
    #     [5, 4444, 59],
    #     [24, 54444, 30],
    #     [24, 24, 30]], 550)
    
    

    
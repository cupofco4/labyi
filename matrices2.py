import math

def find_and_modify_matrix(A):
    n = len(A)
    found = False
    result = None

    # Схема ???
    for i in range(n):
        for j in range(i + 1, n):
            if -math.pi / 2 < A[i][j] and math.pi / 2 > A[i][j]:
                result = math.tan(A[i][j])
                found = True
                break
        if found:
            break


    if found:
        return result

    # Если элемент не найден, создаем одномерный массив X
    X = []
    for i in range(n):
        for j in range(n):
            if i < j and i + j < n - 1:
                X.append(A[i][j])

    return X

A = [
    [1, 0.5, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = find_and_modify_matrix(A)
print("Результат:", result)

# 1. Даны натуральные числа от -500 до 500 Найти все трехзначные числа, у которых четные сотни.
# 2. Дано целое число N (> 1). Найти первое число Фибоначчи, большее N (while)
# 3. Прогрессия

# 1. =============================================
from math import sqrt, sin, cos

def even_hundreds():
    for i in range(-500, 501):
        if abs(i) // 100 % 2 == 0:
            print(i, end=' ')

# 2. =============================================  
def fibonnacci_nums(N):
    if N <= 1:
        return -1
    
    a, b = 0, 1
    while(b <= N):
        a, b = b, a + b
            
    return b

# 3. =============================================
def compute_sequence(n, Y0, Y1, Y2):
    
    print(Y0)
    print(Y1)
    print(Y2)
    
    for i in range(3, n):
        Yi = 1/sqrt(Y0 + sin(Y2) ** 2 + cos(Y1) ** 2)
        print(Yi)
        Y0, Y1, Y2 = Y1, Y2, Yi


if __name__ == '__main__':
    compute_sequence(10, 0.5, 0.6, 0.7)


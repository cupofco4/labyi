def is_prime(n):
    # n - число для проверки
    if n <= 1:
        return False
    
    if n == 2 or n == 3:
        return True
    
    for divider in range(2, n):
        if n % divider == 0:
            return False
        
    return True

def identify_prime_numbers():
    prime_nums = []
    for num in range(10, 100):
        if is_prime(num):
            prime_nums.append(num)
    
    return prime_nums

if __name__ == '__main__':
    print(identify_prime_numbers())
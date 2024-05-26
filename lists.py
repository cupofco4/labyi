# =====================================

def fibonnacci_nums(n):
    a, b = 1, 1
    lst_fibonnacci = [a, b]
    for _ in range(n - 2):
        a, b = b, a + b
        lst_fibonnacci.append(b)
    
    return lst_fibonnacci

# ===================================== 
def count_of_negative(nums: list):
    count = 0
    for num in nums:
        if num < 0:
            count += 1
    
    return count

def change_array(nums: list):
    count_negative_nums = count_of_negative(nums)
    for i in range(len(nums)):
        if nums[i] > 0:
            nums[i] = round(nums[i] / nums[i + 1], 2)
    
    return count_negative_nums, nums

# =====================================
def greatest_product(lst):
    greatest_num = lst[1] * lst[0]
    for i in range(2, len(lst)):
        product_of_numbers = lst[i] * lst[i-1]
        if product_of_numbers > greatest_num:
            greatest_num = product_of_numbers
    
    return greatest_num

# ======================================
def check_array(lst: list, value):
    result = "Нет удовлетворяющего результата!"
    for i in range(len(lst)):
        if abs(lst[i]) < value:
            result = "Ответ находится под индексом " + str(i) + "."
            break
    return result
            


if __name__ == '__main__':
    print(check_array([4, 9, -2, 9, -5, 3, 7], 3)) # Есть реузльтат
    print(check_array([4, 9, -2, 9, -5, 3, 7], 1)) # Нет результата
    print(check_array([4, 1, 9, -2, 9, -5, 3, 7], 3)) # Несколько удовлетворяющих результатов (выберится первый)


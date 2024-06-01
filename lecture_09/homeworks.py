# task 1
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def two_digits_sum(num1, num2):
    res = num1 + num2
    return res


# task 2
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def calculate_average(lst):
    if len(lst) == 0:
        return None
    else:
        total = sum(lst)
        aver = total / len(lst)
        return float(aver)


# task 3
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse(initial_string):
    reversed_string = initial_string[::-1]
    return reversed_string


# task 4
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(worlds_list):
    if len(worlds_list) == 0:
        return None
    else:
        long_word = worlds_list[0]
        for word in worlds_list:
            if len(word) > len(long_word):
                long_word = word
        return long_word


# task 5
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
def sum_of_even_numbers_in_list(lst):
    # Initialize a variable to store the sum of even numbers
    lst_sum = 0
    # Iterate through each item in the list
    for item in lst:
        # Check if the current item is even
        if item % 2 == 0:
            # If the item is even, add it to the sum
            lst_sum = lst_sum + item
    # Return the sum of even numbers
    return lst_sum

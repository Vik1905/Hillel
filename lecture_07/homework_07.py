# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    multiplier = 1
    while True:
        result = number * multiplier
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1

multiplication_table(3)


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def two_digits_sum(num1, num2):
    res = num1 + num2
    print(str(num1) + "+" + str(num2) + "=" + str(res))

two_digits_sum(5,19)


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def calculate_average(lst):
    if len(lst) == 0:
        return None
    else:
        total = sum(lst)
        aver = total / len(lst)
        print(float(aver))

calculate_average([10,2,3,4,5])


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse(initial_string):
    reversed_string = initial_string[::-1]
    return reversed_string

print(reverse("Hello, World"))


# task 5
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

print(longest_word(['pen', 'pencil', 'book', 'notebook', 'ruler', 'dictionary', 'marker']))


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    if str2 in str1:
        return str1.index(str2)
    else:
        return -1
# test 1
str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7
# test 2
str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
# task 7
# Завдання 1 з ДЗ 6
# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False. Строку отримати за допомогою функції input()
def uniq_symbols_count(text):
    # Check if the length of the text is greater than 10
    if len(text) > 10:
        unique_symbols = 0
        # Count the occurrences of the current symbol in the text
        for symbol in text:
            # If the symbol appears only once, increment the count of unique symbols
            if text.count(symbol) == 1:
                unique_symbols += 1
                # If there are more than 10 unique symbols, return True
                if unique_symbols > 10:
                    return True
        # If the count of unique symbols is 10 or less, return False
        if unique_symbols <= 10:
            return False
    # If the length of the text is 10 or less, return False
    else:
        return False

print(uniq_symbols_count(input('Enter your text: ')))

# task 8
# Завдання 3 з ДЗ 6
# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1. Данні в лісті можуть бути будь якими
def leave_string_only(lst1):
    # Initialize an empty list to store string elements
    lst2 = []
    # Iterate through each item in the input list
    for item in lst1:
        # Check if the current item is a string
        if isinstance(item, str):
            # If the item is a string, append it to the new list
            lst2.append(item)
    # Return the new list containing only string elements
    return lst2

print(leave_string_only(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']))


# task 9
# Завдання 4 з ДЗ 6
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

print("Сума усіх парних чисел у списку дорівнює: " + str(sum_of_even_numbers_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])))

# task 10
# Завдання 2 з ДЗ 4
# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".
# P.S. - завдання трошки змінив. Зробив перевірку на наявнісь вказаної літери у тексті
def check_letter_in_word(letter, text):
    # Iterate through each character in the text
    for i in text:
        # Check if the current character matches the letter (case insensitive)
        if i.lower() == letter or i.upper() == letter:
            # If a match is found, return True
            return True
    # If the letter is not found in the text, return False
    return False

print(str(check_letter_in_word('Q', 'Hello, Word!')))


"""  Додаткові завдання:  """

# Task 01
# Рядок відформатованої дати:
"""Ваше завдання - написати функцію, яка отримує дату у вигляді трьох чисел: день, місяць та рік та має на вході розподілювач за замовчанням - "." функція повертає рядок у вигляді "день.місяць.рік". Наприклад, для дати 15 березня 2023 року функція
повинна повертати рядок "15.03.2023". Якщо користувач задає сепаратор відмінний від звичайного, наприклад '/',
то функція повертає "15/03/2023"
Підказка: допоможе використання методу .join():
"""
def format_date(day, month, year, separator='.'):

    # Формуємо рядок з числами дня, місяця і року, розділені вказаним розділювачем
    formatted_date = separator.join([str(day), str(month).zfill(2), str(year)])
    # Повертаємо сформований рядок
    return formatted_date

# test 1
print(format_date(15, 3, 2023))
# test 2
print(format_date(15, 3, 2023, '/'))

# P.S. Виконав завдання саме вихотячі з умови в задачі "написати функцію, яка отримує дату у вигляді трьох чисел".
# Хоча в прикладі вказано місяць строкою "Наприклад, для дати 15 березня 2023 року функція..."
# Можна було приймати місяць і строкою та повертати інтом (наприклад отримувати інт з назви місяця по доданому словнику, або є пошукати відповідну функію якщо така є)


# Task 02
# Порівняння словників:
"""Ваше завдання - написати функцію, яка порівнює два словника, представляючи оцінки студентів за курси. Кожен словник має структуру {'ПІБ студента': оцінка}. Функція повинна порівнювати оцінки студентів за кожний предмет та повертати словник з різницею в оцінках для кожного студента.

```
def compare_grades(grades1, grades2):
    # Ваш код тут
    pass
```

# Приклад використання функції:
grades_1 = {'Анна Коваленко': 90, 'Олег Петров': 85, 'Ірина Сидорова': 78}
grades_2 = {'Анна Коваленко': 92, 'Олег Петров': 87, 'Ірина Сидорова': 80}

result = compare_grades(grades_1, grades_2)
print(result)
# Можливий вивід: {'Анна Коваленко': -2, 'Олег Петров': -2, 'Ірина Сидорова': -2}

Вимоги:
    Функція повинна приймати два аргументи — словники з оцінками студентів (grades1 та grades2).
    Функція повинна порівнювати оцінки за кожним ключем (ПІБ студента) та повертати словник, в якому ключами є ПІБ студентів, а значеннями — різниця в оцінках між grades1 та grades2.
    Виведіть результат для прикладу використання функції.
    Перевірте функцію на кількох тестових вхідних даних, включаючи випадки, коли студенти отримали різні оцінки або коли є студенти, які взагалі не мають оцінок в одному зі словників.
    
"""
def compare_grades(grades1, grades2):
    # Initialize an empty dictionary to store the differences in grades
    grade_differences = {}
    # Iterate through each student in grades1
    for student, grade1 in grades1.items():
        # Check if the student is also in grades2
        if student in grades2:
            # Calculate the difference in grades and store it in the dictionary
            grade_differences[student] = grades2[student] - grade1
        else:
            # If the student is not in grades2, assign None as the difference
            grade_differences[student] = None
    # Iterate through each student in grades2 that is not in grades1
    for student, grade2 in grades2.items():
        if student not in grades1:
            # If the student is not in grades1, assign None as the difference
            grade_differences[student] = None

    # Return the dictionary containing the differences in grades
    return grade_differences


# Test 1:
grades_1 = {'Анна Коваленко': 90, 'Олег Петров': 95}
grades_2 = {'Анна Коваленко': 92, 'Олег Петров': 87, 'Ірина Сидорова': 80}

result = compare_grades(grades_1, grades_2)
print(result)

# Test 2:
grades_1 = {'Анна Коваленко': 90, 'Олег Петров': 85, 'Ірина Сидорова': 78}
grades_2 = {'Олег Петров': 97, 'Ірина Сидорова': 80, 'Олександр Іванов': 93}

result = compare_grades(grades_1, grades_2)
print(result)

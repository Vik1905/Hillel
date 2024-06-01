# Task 1
# Назва
# Рахування унікальних символів в строці
# Опис ДЗ
# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False. Строку отримати за допомогою функції input()

text = input('Enter your text: ')
result = False
if len(text) > 10:                           # Перевірка що строка має більше 10 символів, інакше немає сенсу щось перевіряти далі
    unique_symbols = 0
    for symbol in text:
        if text.count(symbol) == 1:
            unique_symbols += 1
            if unique_symbols > 10:         # Перевірка що кількість унікальних символів більше десяти. Якщо виконується, зупиняю виконнаня коду.
                result = True
                break
print(result)


# Task 2
# Назва
# Цикл “Дочекайся літери”
# Опис ДЗ
# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h" (враховуються як великі так і маленькі). Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

h_absent = True
while h_absent:
    text = input('Type your text with \'h/H\' letter: ')
    for i in text:
        if i == 'h' or i == 'H':
            h_absent = False


# Task 3
# Назва
# Забери зі списку що потрібно
# Опис ДЗ
# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1. Данні в лісті можуть бути будь якими

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for item in lst1:
    if isinstance(item, str):
        lst2.append(item)
print(lst2)


# Task 4
# Назва
# Сумуємо числа
# Опис ДЗ
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
lst_sum = 0
for item in lst:
    if item % 2 == 0:
        lst_sum = lst_sum + item
print(lst_sum)

# Task 1
# Візміть два файли з теки
# ideas_for_test/work_with_csv
# порівняйте на наявність дублікатів і приберіть їх.
# Результат запишіть у файл result_<your_second_name>.csv

import csv

# Функція для зчитування CSV-файлу
def read_csv(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        return list(reader)

# Функція для видалення порожніх колонок з кінця рядка. Потрібна так як Python вважає рядки різними якщо в одному з них в кінці є порожні колонки
def trim_empty_columns(row):
    while row and row[-1] == '':
        row.pop()
    return row

file1 = read_csv('CSV_data/random.csv')
file2 = read_csv('CSV_data/random-michaels.csv')

# Видалення порожніх колонок з заголовків
header1 = trim_empty_columns(file1[0])
header2 = trim_empty_columns(file2[0])

# Перевірка на однаковість заголовків
if header1 != header2:
    print('The headers in the files are not the same. Unification is not possible.')
else:
    header = header1
    # Видалення порожніх колонок з рядків даних
    rows1 = trim_empty_columns(file1[1:])
    rows2 = trim_empty_columns(file2[1:])

    # Об'єднання рядків з обох файлів
    all_rows = file1[1:] + file2[1:]
    all_rows.insert(0, header)

    # Пошук унікальних рядків
    unique_rows = []
    for row in all_rows:
        if row not in unique_rows:
            unique_rows.append(row)

    # Запис унікальних рядків у новий CSV-файл
    with open('CSV_data/result_Kirikov.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(unique_rows)
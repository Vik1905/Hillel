# Task 2
# Провалідуйте, чи усі файли у папці
# ideas_for_test/work_with_json
# є валідними json.
# результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log

import json
from pathlib import Path
import logging

# Налаштування логера
logging.basicConfig(filename='json_Kirikov.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Вказання шляху до директорії з JSON файлами
path = Path('json_data')

# Отримання списку файлів у директорії
files = [f for f in path.iterdir() if f.is_file()]

# Перевірка кожного файлу в директорії
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        try:
            json.load(file)
        except json.JSONDecodeError as e:
            logging.error(f"Invalid JSON file: {f} - {str(e)}")
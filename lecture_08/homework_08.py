def sum_of_numbers(string):
    try:
        # Розділяємо рядок, кожен елемент конвертуємо у число(int) і записуємо у список, потім рахуємо і повертаємо суму чисел зі списку
        numbers = []
        for number in string.split(","):
            numbers.append(int(number))
        return sum(numbers)
    except ValueError:
        # Якщо виникає помилка при конвертації в число, виводимо повідомлення про помилку
        return "Не можу це зробити!"

# Заданий масив рядків з числами, розділеними комами
strings = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

# Проходимося по кожному рядку і виводимо суму чисел
for string in strings:
    print(sum_of_numbers(string))

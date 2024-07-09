# Генератори:
# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
def even_nums(n):
    for i in range(0, n+1, 2):
        yield i

# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
def fibonacci(n):
    a, b = 0, 1
    while a <=n:
        yield a
        a, b = b, a+b


# Ітератори:
# Реалізуйте ітератор для зворотного виведення елементів списку.
class ReverseListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        else:
            self.index -= 1
            return self.lst[self.index]

# Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
class EvenNumberIterator:
    def __init__(self, n):
        self.n = n
        self.current_value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_value < self.n:
            self.current_value += 2
            return self.current_value
        else:
            raise StopIteration


# Декоратори:
# Напишіть декоратор, який логує аргументи та результати викликаної функції.
def log_arguments_and_results(func):
    def wrapper(*args, **kwargs):
        print(f"Виклик функції {func.__name__} з аргументами: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат функції {func.__name__}: {result}")
        return result
    return wrapper

# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Виникла помилка: {e}")
    return wrapper

# Task 1
# Об’єктний студент
# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючи студента.
# Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
# Виведіть інформацію про студента та змініть його середній бал.

class Student:
    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.__average_grade = average_grade

    def set_new_average_grade(self, new_grade):
        if type(new_grade) not in [int, float]:
            raise ValueError('Specified value is not a number!')
        self.__average_grade = new_grade

    def display_info(self):
        print(f"Студент: {self.first_name} {self.last_name}, Вік: {self.age}, Середній бал: {self.__average_grade}")


# Створення об'єкта класу "Студент"
student = Student("Іван", "Іваненко", 20, 4.5)

# Виведення інформації про студента
student.display_info()

# Зміна середнього балу студента
student.set_new_average_grade(4.7)

# Виведення оновленої інформації про студента
student.display_info()


# Task 2
# Бібліотека
# Створіть клас "Бібліотека", який буде представляти собою колекцію книг.
# Додайте метод add_book() до класу "Бібліотека", який дозволяє додавати нові книги до колекції.
# Створіть метод get_books(), котрий буде повертати усі книги з бібліотеки.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise ValueError("Invalid book object")
    def get_books(self):
        return self.books


# Приклад використання:
library = Library()
book1 = Book("The classics of Ukrainian literature", "Taras Shevchenko")
book2 = Book("War and Peace", "Leo Tolstoy")

library.add_book(book1)
library.add_book(book2)

for book in library.get_books():
    print(f"Назва: {book.title}, Автор: {book.author}")


# Task 3
# Банківський рахунок
# Створіть клас "BankAccount".
# Реалізуйте атрибути, які представляють основну інформацію про рахунок (номер рахунку та баланс). Доступ до цих атрибутів повинен бути тільки через методи класу.
# Створіть методи для отримання та встановлення цих значень.

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number):
        if type(account_number) is not int:
            raise ValueError("Invalid account number. The account number must be integer type")
        self.__account_number = account_number

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if type(balance) not in [int, float]:
            raise ValueError("Invalid balance value. The balance value must consist of numbers only")
        self.__balance = balance


# Приклад використання:
account1 = BankAccount(123456789, 1200)

print(f"Номер рахунку: {account1.get_account_number()}, Залишок коштів: {account1.get_balance()}")

account1.set_account_number(147852369)
account1.set_balance(3350)

print(f"Номер рахунку: {account1.get_account_number()}, Залишок коштів: {account1.get_balance()}")

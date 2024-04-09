# alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

# task 01 result
alice_in_wonderland = '''
"Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don't much care where ——" said Alice.
"Then it doesn't matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."
'''

# task 02 result
alice_in_wonderland = alice_in_wonderland.replace("'", "\'")  # екранування одинарних лапок (не знайшов дужок в тексті, тож вирішив що в завданні помилка і малися на увазі лапки)

# task 03 result
print("\nРішення задач №1, 2, 3:")
print(alice_in_wonderland)


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
# task 04 result
print("Рішення задачі №4:")
black_sea_area = 436402
azov_sea_area = 37800
total_area = black_sea_area + azov_sea_area
print("Площа Чорного та Азовського морів разом становить:", total_area, "км^2")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
# task 05 result
print("\nРішення задачі №5:")
total_goods = 375291
first_plus_second = 250449
second_plus_third = 222950

first_storage = (first_plus_second - second_plus_third) / 2
second_storage = first_plus_second - first_storage
third_storage = total_goods - first_plus_second - second_plus_third + second_storage
print("Кількість товарів на першому складі:", first_storage)
print("Кількість товарів на другому складі:", second_storage)
print("Кількість товарів на третьому складі:", third_storage)


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
# task 06 result
print("\nРішення задачі №6:")
monthly_payment = 1179  # грн
payment_period = 1.5     # роки
computer_cost = monthly_payment * payment_period * 12
print("Вартість комп'ютера становить:", computer_cost, "грн")


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
# task 07 result
print("\nРішення задачі №7:")
numbers = [8019, 9907, 2789, 7248, 7128, 19224]
divisors = [8, 9, 5, 6, 5, 9]
remainders = [numbers[i] % divisors[i] for i in range(len(numbers))]
print("Остачі від ділення:")
for i in range(len(numbers)):
    print(numbers[i], ":", divisors[i], "=", remainders[i])


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
# task 08 result
print("\nРішення задачі №8:")
pizza_large = 274  # грн
pizza_medium = 218  # грн
juice = 35  # грн
cake = 350  # грн
water = 21  # грн

order = {
    "Піца велика": 4 * pizza_large,
    "Піца середня": 2 * pizza_medium,
    "Сік": 4 * juice,
    "Торт": cake,
    "Вода": 3 * water
}

total_cost = sum(order.values())
print("Загальна вартість замовлення:", total_cost, "грн")


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
# task 09 result
print("\nРішення задачі №9:")
total_photos = 232
photos_per_page = 8
pages = int(total_photos / photos_per_page)
if total_photos % photos_per_page > 0:
    pages += 1
print("Ігорю знадобиться", pages, "сторінок для вклеювання всіх фотографій.")


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
# task 10 result
print("\nРішення задачі №10:")
total_distance = 1600
fuel_consumption_per_km = 9 / 100
total_fuel_consumption = total_distance * fuel_consumption_per_km
print("Для автомобільної подорожі із Харкова в Будапешт потрібно", total_fuel_consumption, "літрів бензину.")
count_of_refills = int(total_fuel_consumption / 48)
if total_fuel_consumption % 48 > 0:
    count_of_refills += 1
print("Для подорожі знадобиться щонайменше", count_of_refills, "рази заправляти авто.")

# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13 # have age >=30. Print condition check result


people_records = [
    ('John', 'Doe', 28, 'Engineer', 'New York'),
    ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
    ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
    ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
    ('Michael', 'Brown', 22, 'Student', 'Seattle'),
    ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
    ('David', 'Miller', 33, 'Software Developer', 'Austin'),
    ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
    ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
    ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
    ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
    ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
    ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
    ('Ava', 'White', 42, 'Journalist', 'San Diego'),
    ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

# Task 1 - Add your new record o the beginning of the given list
new_record = ('Gordon', 'Freeman', 27, 'Engineer', 'Seattle')
people_records.insert(0, new_record)

# Task 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
print("\nTask 2 result:")
people_records[1], people_records[5] = people_records[5], people_records[1]
for i in people_records:
    print(i)   # також можна вивести кортеж через print(people_records), але виведення циклом по єлементам виглядає краще

# Task 3 - check that all people in modified list with records indexes 6, 10, 13 # have age >=30. Print condition check result
print("\nTask 3 result:")
indexes = [6, 10, 13]
all_above_30 = None
for i in indexes:
    if people_records[i][2] >= 30:
        all_above_30 = True
    else:
        all_above_30 = False
        break

print("Are all people at indexes 6, 10, 13 above or equal to 30 years old?", all_above_30)
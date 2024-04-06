adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
# task 01 result
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")


# task 02 ==
""" Замініть .... на пробіл
"""
# task 02 result
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")


# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
# task 03 result
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
# task 04 result
count_h = adwentures_of_tom_sawer.count("h")
print("Task 04: Літера \"h\" зустрічаеться", count_h, "разів.")


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
# task 05 result
words = adwentures_of_tom_sawer.split()
count_uppercase = 0
for word in words:
    if word[0].isupper():
        count_uppercase += 1
print("Task 05:", count_uppercase, "слів у тексті починаються з великої літери.")


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
# task 06 result
tom_index = adwentures_of_tom_sawer.find("Tom")
if tom_index is not None:
    second_index = adwentures_of_tom_sawer.find("Tom", tom_index + 1)
print("Task 06: Слово Tom зустрічається вдруге на позиції:", tom_index)


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
# task 07 result
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(". ")


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
# task 08 result
print("Task 08:", adwentures_of_tom_sawer_sentences[3].lower())


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
# task 09 result
startsWithByTheTime = False
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith("By the time"):
        startsWithByTheTime = True
        break
print("Task 09: В тексті речення яке починається з \"By the time\":", startsWithByTheTime)


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
# task 10 result
last_sentence_words_count = len(adwentures_of_tom_sawer_sentences[-1].split())
print("Task 10: В останньому реченні кількість слів =", last_sentence_words_count)

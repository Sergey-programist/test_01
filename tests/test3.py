'''
Соня и Вася едут в поезде и проводят время за игрой.
Соня загадала два разных предмета.
Вася должен их угадать. Порядок, в котором он должен это сделать, не важен.
Даны строки s_word1 и s_word2 (Сонины слова) и v_word1 и v_word2 (Васины ответы).
Угадал ли Вася? Выведи "ДА" или "НЕТ".
'''

sonja_word_one = input().lower()
sonja_word_two = input().lower()
sonja_words = (sonja_word_one, sonja_word_two)

vasja_word_one = input().lower()
vasja_word_two = input().lower()
sonja_has_words = (vasja_word_one in sonja_words) and (vasja_word_two in sonja_words)

if sonja_has_words:
    print("Да")
else:
    print("Нет")


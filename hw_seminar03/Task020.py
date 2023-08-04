# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ●A, E, I, O, U, L, N, S, T, R – 1 очко;
# ●D, G – 2 очка;
# ●B, C, M, P – 3 очка;
# ●F, H, V, W, Y – 4 очка;
# ●K – 5 очков;
# ●J, X – 8 очков;
# ●Q, Z – 10 очков.
#
# А русские буквы оцениваются так:
# ●А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ●Д, К, Л, М, П, У – 2 очка;
# ●Б, Г, Ё, Ь, Я – 3 очка;
# ●Й, Ы – 4 очка;
# ●Ж, З, Х, Ц, Ч – 5 очков;
# ●Ш, Э, Ю – 8 очков;
# ●Ф, Щ, Ъ – 10 очков.
#
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо
# только английские, либо только русские буквы.

#k = input('Введите слово: ')
#k = word.upper()
k='ноутбук'
dict_1 = {1: 'A,E,I,O,U,L,N,S,T,R,А, В, Е, И, Н, О, Р, С, Т',
          2: 'D, G, Д, К, Л, М, П, У',
          3: 'B, C, M, P, Б, Г, Ё, Ь, Я',
          4: 'F, H, V, W, Y, Й, Ы',
          5: 'K, Ж, З, Х, Ц, Ч',
          8: 'J, X, Ш, Э, Ю',
          10: 'Q, Z, Ф, Щ, Ъ'}

count = 0
for i in k:
    for key, value in dict_1.items():
        if i.upper() in value:
            count = count+key
print(count)

#print(word)

points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
word = k.upper()  # переводим все буквы в верхний регистр
count = 0
for i in word:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        for j in points_en:
            if i in points_en[j]:
                count = count + j
    else:
        for j in points_en:
            if i in points_ru[j]:
                count = count + j
print(count)

alpha = {'AEIOULNSTRАВЕИНОРСТ': 1,
         'DGДКЛМПУ': 2,
         'BCMPБГЁЬЯ': 3,
         'FHVWYЙЫ': 4,
         'KЖЗХЦЧ': 5,
         'JXШЭЮ': 8,
         'QZФЩЪ': 10}

word = input('Введите слово: ')
total = 0
new_alpha = {}
for letters, score in alpha.items():
    new_alpha.update(dict.fromkeys(letters, score))

for char in word.upper():
    total += new_alpha.get(char)

# for char in word.upper():
#     for letters, score in alpha.items():
#         if char in letters:
#             total += score

print(f'Слово {word} весит {total} очков')
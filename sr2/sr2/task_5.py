# Есть словарь песен группы Depeche Mode violator
# songsdict = {'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30,
#              'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6,
#              'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68, }
# Выведите общее время звучания всех песен.Создайте список песен,
# время звучаниях которых больше 5 минут Создайте новый словарь тех песен, в название которых состоит из одного слова

songsdict = {'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30,
             'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6,
             'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68, }
all_time = 0
for value in songsdict.values():
    all_time += value
print(all_time)
five_min = []
for key,value in songsdict.items():
    if value > 5:
        five_min.append(key)
print(five_min)
one_word_songs = {}
for key,value in songsdict.items():
    if ' ' not in key:
        one_word_songs[key] = value
print(one_word_songs)

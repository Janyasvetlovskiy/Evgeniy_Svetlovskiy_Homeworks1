# 5)	Выведите статистику частности букв в кортеже
# long_word = ( 'т', 'т', 'а', 'и', 'и', 'а', 'и’,'и', 'и', 'т', 'т', 'а', 'и', 'и','и', 'и', 'и', 'т', 'и’)
# Примечание: Статистика частности - число повторений каждой из букв.
long_word = ( 'т', 'т', 'а', 'и', 'и', 'а', 'и','и', 'и', 'т', 'т', 'а', 'и', 'и','и', 'и', 'и', 'т', 'и')
stats = {key: long_word.count(key) for key in long_word}
print(stats)
# 15.	Необходимо удалить пустые строки из списка строк.
spis = ['table', 'sofa', '', 'home', '', 'hi']
string2 = ' '.join(spis)
string3 = string2.split()
print(string3)
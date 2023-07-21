# 2) Выберите любую папку на своем компьютере, имеющую вложенные директории.
# Выведите на печать в терминал ее содержимое, как и всех подкаталогов(вывести имя папки и имена файлов)

import os

path = r"C:\Users\Smile\PycharmProjects\python\dz fails2\for dz"
lst_path = [path]
while lst_path:
    current_path = lst_path.pop()
    if os.path.isdir(current_path):
        print(os.path.normpath(current_path))
        for folder in os.listdir(current_path):
            child_path = os.path.join(current_path, folder)
            lst_path.append(child_path)
    else:
        print(os.path.normpath(current_path))

# list1 = os.listdir(r'C:\Users\Smile\PycharmProjects\python\dz fails2\for dz')
# result = []
# for elem in os.listdir(list1):
#      if os.path.isfile(os.path.join(list1, elem)):
#          result.append(elem)
# print(result)
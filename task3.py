import os
def save_file(file: str, changes: list, mode: str="w", coding="utf-8"): # Функция для загрузки в файл, принимает двумерный список изменений и имя файла для сохранения
    with open(file, mode, encoding=coding) as saving_file:
        for lists in changes: # Поскольку почился друмерный список, используем вложенный цикл
            for line in lists:
                saving_file.write(line)
            saving_file.write("\n")

def sorting_files(files_dict: dict, mode: str="r", coding: str="utf-8"):
    data = [] # Список, в котором будут содержание файлов
    for names,paths in files_dict.items():
        with open(paths, mode, encoding=coding) as current_file:
            lines_list = current_file.readlines()
            data.append([names + "\n"] + [str(len(lines_list)) + "\n"] + lines_list) # Здесь сразу добавляем имя файла и его длину в начало
            
    data.sort(key=lambda x: len(x)) # Сортируем списки по длине
    save_file(PATH_FOR_SAVE, data) # Вызываем функцию сохранения
            
# Переменные
FILE_PATH = os.getcwd()
DIR = "sort"
filename_1 = "1.txt"
filename_2 = "2.txt"
filename_3 = "3.txt"

# Определяем путь для каждого файла
FILENAME_1_PATH = os.path.join(FILE_PATH, DIR, filename_1) 
FILENAME_2_PATH = os.path.join(FILE_PATH, DIR, filename_2)
FILENAME_3_PATH = os.path.join(FILE_PATH, DIR, filename_3)

# Формируем словарь для дальнейшего использования имен переменных и их путей
FILES_PATH = {filename_1 : FILENAME_1_PATH, filename_2 : FILENAME_2_PATH, filename_3 : FILENAME_3_PATH}

#Переменные для записи в файл 
FILE_FOR_SAVE = 'result.txt'
PATH_FOR_SAVE = os.path.join(FILE_PATH, DIR, FILE_FOR_SAVE)

#Вызов функции
sorting_files(FILES_PATH)

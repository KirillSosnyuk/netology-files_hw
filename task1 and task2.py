import os
def file_load(filename: str, mode: str="w", coding: str="utf-8"): # На всякий случай добавил функцию сохранения результата работы в текстовый файл.
    with open(filename, mode, encoding=coding) as file:
        for dish in cook_book:
            file.write(str(dish) + ":" + str(cook_book[dish]) + "\n")
        file.write("\n")
        for ingredient in ingredients_for_save:
            file.write(str(ingredient) + ":" + str(ingredients_for_save[ingredient]) + "\n")
            
def get_shop_list_by_dishes(dishes, person_count):
    ingredients = {}
    for dish in dishes:
        for components in cook_book[dish]:
            ingredients[components[book_values[0]]] = {book_values[2] : components[book_values[2]], book_values[1] : int(components[book_values[1]]) * person_count}
            
    return ingredients

def file_read(filename: str, mode: str="r", coding: str="utf-8"):
    with open(filename, mode, encoding=coding) as file:
        saver = file.readline()
        while saver != "":
            if saver  == "\n":
                saver = file.readline()
                continue
            
            saver = saver.rstrip()

            if not saver.isdigit() and not "|" in saver:
                cook_book[saver] = []
                dish = saver
            elif saver.isdigit():
                for lines in range(int(saver)):
                    saver = file.readline().rstrip().split(" | ")
                    cook_book[dish].append(dict(zip(book_values, saver)))
                    
            saver = file.readline()
            
    return cook_book



# Сделал глобальными cook_book и book_values для задачи 2 и сохранения в файл.
cook_book = {}
book_values = ['ingredient_name', 'quantity', 'measure']

# Переменные для указания пути к файлам
FILE_PATH = os.getcwd()
DIR = 'files'
FILE_TASK_1 = 'old_recipes_task1.txt'
FULL_PATH_TASK_1 = os.path.join(FILE_PATH, DIR, FILE_TASK_1)
SAVE_FILE = 'new_recipes_task1_and_task2.txt'
FULL_PATH_FOR_SAVE = os.path.join(FILE_PATH, DIR, SAVE_FILE)

# Задача 1
print(file_read(FULL_PATH_TASK_1)) # Тестуем для задачи № 1

#Задача 2
ingredients_for_save = get_shop_list_by_dishes(['Утка по-пекински', 'Фахитос'], 3)
print(ingredients_for_save) # Тестируем для задачи № 2

file_load(FULL_PATH_FOR_SAVE)

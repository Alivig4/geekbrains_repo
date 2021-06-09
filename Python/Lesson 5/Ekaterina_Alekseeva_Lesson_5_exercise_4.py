# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
translation_dict = {"one": "один", "two": "два", "three": "три", "four": "четыре"}
new_file = open("Files/File_Exercise_4_fixed.txt", "w")
for line in open("Files/File_Exercise_4.txt"):
    eng, num = line.split(" — ")
    new_file.write(translation_dict[eng.lower()].capitalize() + " — " + num)
new_file.close()

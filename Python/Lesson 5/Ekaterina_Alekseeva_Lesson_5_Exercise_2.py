# Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

my_file = open("Files/File_Exercise_2.txt", "r")
lines = my_file.readlines()
my_file.close()
print("Количество строк:", len(lines))

for i, line in enumerate(lines):
    words = len(line.split())
    print("Количество слов в строке " + str(i+1) + ": " + str(words))

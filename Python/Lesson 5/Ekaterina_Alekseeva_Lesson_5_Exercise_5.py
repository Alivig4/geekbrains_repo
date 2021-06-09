# Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint

my_file = open("Files/File_Exercise_5.txt", "w")
for i in range(0, 30):
    my_file.write(str(randint(0, 100)) + (" " if i < 29 else ""))
my_file.close()

total = 0
for line in open("Files/File_Exercise_5.txt"):
    for num in line.split(" "):
        total += int(num)

print("Результат:", total)
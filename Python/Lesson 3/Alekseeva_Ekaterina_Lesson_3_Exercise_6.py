# Реализовать функцию int_func(),
# принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
#
# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func(word):
    return word.capitalize()


def int_func_multi(sentence):
    return_value = ""
    for word in sentence.split():
        return_value += int_func(word) + " "
    return return_value


print(int_func("рЕзУлЬтАт:"), int_func_multi(input("Введите строку: ")))
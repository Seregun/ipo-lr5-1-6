with open('E:\\Python\\lr5_6\\text.txt', 'r') as file: # Открытие файла text.txt (указать путь к файлу) для чтения
    lines = file.readlines()  # Чтение всех строк из файла и сохранение их в переменной lines
with open('output.txt', 'w') as output_file: # Открытие нового файла output.txt для записи
    for i, line in enumerate(lines, 1):  # Использование функции enumerate для получения номера строки
        output_line = f"{i}: {line}"  # Добавление номера строки перед каждой строкой
        output_file.write(output_line)  # Записывание строки в новый файл
        print(output_line)  # Вывод результата

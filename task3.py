files = ['1.txt', '2.txt', '3.txt']  # Создаем список файлов вручную

def count_lines(file_name):  # Определяем функцию для получения количества строк в файле
    with open(file_name, 'r') as f:
        return sum(1 for line in f)

files.sort(key=count_lines)  # Сортируем файлы по количеству строк в них

with open('united_file.txt', 'w') as united_file:  # Открываем новый файл для записи
    for file_name in files:  # Обходим отсортированные файлы
        united_file.write(f'{file_name}\n')  # Записываем служебную информацию (имя файла и количество строк)
        united_file.write(f'{count_lines(file_name)}\n')
        
        with open(file_name, 'r') as current_file:  # Записываем содержимое файла
            for line in current_file:
                united_file.write(line)

        united_file.write('\n' + '\n')
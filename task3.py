def read_file(file_name):  #функция для считывания
    with open(file_name, 'r') as file:
        content = file.readlines()
    return content

def write_united(file_names, output_file):  #функция для записи
    with open(output_file, 'w') as output:
        for file_name in file_names:
            content = read_file(file_name)
            output.write(f'{file_name}\n')
            output.write(f'{len(content)}\n')
            output.write('\n')
            output.writelines(content)
            output.write("\n\n")

file_names = ['1.txt', '2.txt', '3.txt']  #файлы
output_file = 'united_file.txt'  #выходной файл

write_united(file_names, output_file)  #объявление функции

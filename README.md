 # Скрипт конвертации медиафайлов в директории с помощью ffmpeg
 * С помощью медота get_final_files мы получаем путь к файлам в директориях любой структуры и добавляем в список только те файлы у которых размер больше 10 ГБ.
 * В методе extract_info мы создаем словарь вида  {'FilePath': file_path, 'FileSize': size}
 * Методом save_to_json сохраняем информацию в json файл
 * Дальше создается метод covert_video для конвертации файла с помощью модуля subprocess и ffmpeg
 * Далее создается фунцкия main с точкой входа в которой:
 	+ вызываются методы  get_final_files, extract_info и save_to_json для создания файла file_info.json со списком параметров файла (путь к файлу, размер)
 	+ вызывается медот covert_video и добавляется в файл file_info.json состояние файлы (Конвертация, Файл сконвертирован, NewFilePath(новый путь к файлу, так как extensions файла мог изменится))
 * Создается точка входа скрипта 

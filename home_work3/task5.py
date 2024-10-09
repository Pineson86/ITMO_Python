#В коде указаны абсолютные пути для файлов, так как у меня интепретатор почему-то запускается не в папке, где скрипт, а в главной папке '/users'

# Paths of export files
path1 = r"C:\Users\User\Documents\Codding\Python\ITMO_Python\home_work3\text1.txt"
path2 = r"C:\Users\User\Documents\Codding\Python\ITMO_Python\home_work3\text2.txt"
path3 = r"C:\Users\User\Documents\Codding\Python\ITMO_Python\home_work3\text3.txt"

#Creating list of file paths
paths = []
paths.extend([path1, path2, path3])

#path of import file
import_file_path = r"C:\Users\User\Documents\Codding\Python\ITMO_Python\home_work3\text4.txt"

#Mode for function merge_files: write of not write merged string to a file
write_to_file = True
def merge_files(paths, rite_to_file):
    merged_string = ''
    for k in range(len(paths)):
        with open(paths[k], 'r', encoding='utf-8') as f:
            content = f.read()
            merged_string += content
    if write_to_file == True:
        with open(import_file_path, 'w',  encoding='utf-8') as file:
            file.write(merged_string)
        return f'Next note has been writen to file: {merged_string}'
    else:
        return f'Next string as been exported from the files: {merged_string}'

print(merge_files(paths, write_to_file))
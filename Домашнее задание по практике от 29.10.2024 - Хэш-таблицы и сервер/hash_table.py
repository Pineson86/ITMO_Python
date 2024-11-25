#Статическая хеш-таблица размером 256. Разрешение коллизий реализуется методом цепочек
class Hash_Table:
    def __init__(self, size = 256):
        self.table = [None] * 256
        self.size = size

    def hash_func(self, target):
        index = sum(ord(char) for char in target) % self.size
        return index


    def insert_value(self):
        while True:
            target = input('Введите слово, которое хотите добавить в хранилище или напишите "stop", чтобы выйти: ')
            if target == 'stop':
                break
            index = self.hash_func(target) #Получаем индекс для всавки значения в таблицу
            if self.table[index] is None: #Проверяем не занят ли уже этот индекс
                self.table[index] = [target]#Если не  занят, создаем список и  вставляем туда введенное значение в качестве первого элемента
            else:
                self.table[index].append(target) #Если под данным индексом уже есть что-то, то добавляем введенное значение в список

#Пример реализиации
hash_table = Hash_Table()
hash_table.insert_value()
print(hash_table.table)
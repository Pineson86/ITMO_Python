words = ["солнце", "дерево", "океан", "гора", "музыка", "цветок", "корабль", "звезда", "песок", "луна", "ветер", "город", "река", "небо", "лес"]

#Получаем список весов слов из их юникодов
word_weights = []
for word in words:
    word_weight = 0
    for char in word:
        unicode_char = ord(char)
        word_weight += unicode_char
    word_weights.append(word_weight)

#Сортируем
word_weights= sorted(word_weights)

#Организуем бинарный поиск через функцию
def find_weight_in_list(weights, target_word):
    def calculate_word_weight(word):
        """Вычисляет вес слова как сумму Unicode значений его символов."""
        return sum(ord(char) for char in word)

    target_weight = calculate_word_weight(target_word)  # Получаем вес искомого слова
    left, right = 0, len(weights) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if weights[mid] == target_weight:
            return target_weight, target_word, mid  # Возвращаем вес, слово и индекс
        elif weights[mid] < target_weight:
            left = mid + 1
        else:
            right = mid - 1
    
    return None  # Если вес не найден

user_word = input("Введите слово для поиска: ")
result = find_weight_in_list(word_weights, user_word)

if result:
    weight, word, index = result
    print(f"Слово '{word}' найдено с весом {weight} на индексе {index}.")
else:
    print("Слово не найдено.")

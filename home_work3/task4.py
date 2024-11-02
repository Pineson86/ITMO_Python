import string

with open(r"C:\Users\User\Documents\Codding\Python\ITMO_Python\home_work3\text1.txt", 'r', encoding='utf-8') as f:#У меня на компьютере почему-то читаются Питоном только при указания прямого пути. И еще без последнего параметра получается почему-то какая-то ерунда!
    #Counting lines
    def line_counter(f):
        content = f.read() #Reading all file content in one string
        string_num = content.count('\n') + 1
        return string_num

    #print(line_counter(f))

    f.seek(0)#Put cursor in the beginning of the file

    #Another way of counting lines
    def line_counter(f):
        counter = 0
        for line in f:
            counter += 1
        return counter

    print(f'The line number in the text : {line_counter(f)}')

    f.seek(0)#Put cursor in the beginning of the file

    #Counting symbols in the line
    def symbols_counting(f):
        counter = 0
        for line in f:
            for char in line:
                if char != '\n':
                    counter += 1
        return counter

    print(f'The symbols number in the text: {symbols_counting(f)}')

    f.seek(0)#Put cursor in the beginning of the file

    #Counting words
    def word_counter(f):
        content = f.read()
        words = content.split()
        #cleaning words from punctuation marks
        words = [word.strip(string.punctuation) for word in words]
        return words, len(words)

    words, word_amount= word_counter(f)
    print(f'The words number in the text: {word_amount}')

    #Finding the longest word in the text
    def longest_word_finder(words):
        words_length_dict = dict()
        for word in words:
            words_length_dict[word] = len(word)
        sorted_length_words = dict(sorted(words_length_dict.items(), key=lambda item: item[1], reverse = True))
        return list(sorted_length_words.keys())[0]

    print(f'The longest word in the text is {longest_word_finder(words)}')
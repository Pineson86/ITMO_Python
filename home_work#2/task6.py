s = "Мистер и миссис Дурсль проживали в доме номер четыре по Тисовой улице и всегда с гордостью заявляли, что они, слава богу, абсолютно нормальные люди. Уж от кого-кого, а от них никак нельзя было ожидать, чтобы они попали в какую-нибудь странную или загадочную ситуацию. Мистер и миссис Дурсль весьма неодобрительно относились к любым странностям, загадкам и прочей ерунде."
#Lower case letters only
s = s.lower()

#Removing punctuation marks
s_without_puntuation = ''
for char in s:
    if char != '.' and char != ',':
        s_without_puntuation += char
print(s_without_puntuation)

#getting a list of words from the string
words_list = s_without_puntuation.split()
print(words_list)

#Creating a dictionary with counted words
counted_words_dict = {}
counter = 0
for word in words_list:
    counted_words_dict[word] = 0
for key in counted_words_dict.keys():
    for word in words_list:
        if word == key:
            counter += 1
    counted_words_dict[key] = counter
    counter = 0

#Sorting dictionary by value starting from biggest
counted_words_dict = dict(sorted(counted_words_dict.items(), key=lambda item: item[1], reverse=True))
print(counted_words_dict)
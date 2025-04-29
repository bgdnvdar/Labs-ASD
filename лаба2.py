import re

def words(wrd):
    words = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
        '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'}
    return ' '.join(words[n] for n in wrd)

f = open('txt.txt', 'r')
file = f.read()
lst = [x for x in file.split()]
k = 1

for lexeme in lst:
    if re.match(r'^21/d+$', lexeme):
        c = 1
        for i in range(1, len(lexeme)):
            if lexeme[i] == lexeme[i - 1]:
                c += 1
            else:
                if c > k:
                    print(lexeme, words(str(lexeme[i - 1])), c)
                c = 1
        if c > k:
            print(lexeme, words(str(lexeme[-1])), c)
f.close()




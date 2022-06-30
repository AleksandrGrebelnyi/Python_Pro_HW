# 1. Create a class that performs statistical processing of a text file - counting characters, words, sentences, etc.
# Determine the required attributes-data and attributes-methods in class for working with the text file.
import os
from exception_for_text import EmptyFile

class WorkWithText:

    def __init__(self):
        pass

    def number_of_words(self):
        with open('some_text.txt', 'r', encoding='utf-8') as f:
            data = f.readline()
            res = 0
            while data:
                res += data.count(' ')
                data = f.readline()
        return res

    def amount_of_strings(self):
        with open('some_text.txt', 'r', encoding='utf-8') as f:
            data = f.readline()
            count = 1
            while data:
                for i in data:
                    if '\n' in i:
                        count += 1
                data = f.readline()
        return count


    def number_of_symbols(self):
        with open('some_text.txt', 'r', encoding='utf-8') as f:
            data = f.readline()
            count = 0
            while data:
                for i in data:
                    count += len(i)
                data = f.readline()
        return count

    def num_of_symbols_without_spaces(self):
        with open('some_text.txt', 'r', encoding='utf-8') as f:
            data = f.readline()
            count = 0
            while data:
                for i in data:
                    count += len(i)
                data = f.readline()
        return count - WorkWithText.number_of_words(res)

    def amount_of_sentence(self):
        with open('some_text.txt', 'r', encoding='utf-8') as f:
            data = f.readline()
            count = 1
            while data:
                count += data.count('. ')
                data = f.readline()
        return count

    def how_many_points(self):
        with open('some_text.txt', 'r', encoding='utf-8') as f:
            data = f.readline()
            count = 0
            while data:
                count += data.count('.')
                data = f.readline()
        return count

    def how_many_numbers(self):
        with open('some_text.txt', 'r', encoding='utf-8') as f:
            data = f.readline()
            count = 0
            while data:
                for num in data:
                    if num.isdigit():
                        count += 1
                data = f.readline()
        return count

    def how_many_dashes(self):
        with open('some_text.txt', 'r', encoding='utf-8') as f:
            data = f.readline()
            count = 0
            while data:
                for dash in data:
                    if '-' in dash:
                        count += 1
                data = f.readline()
        return count

    def __str__(self):
        res = f'Number of words: {self.number_of_words()}\n'
        res += f'Amount of strings: {self.amount_of_strings()}\n'
        res += f'Number of symbols: {self.number_of_symbols()}\n'
        res += f'Number of symbols without spaces: {self.num_of_symbols_without_spaces()}\n'
        res += f'Amount of sentence: {self.amount_of_sentence()}\n'
        res += f'Amount of points: {self.how_many_points()}\n'
        res += f'Amount of numbers: {self.how_many_numbers()}\n'
        res += f"Amount of '-': {self.how_many_dashes()}"
        return res

if __name__ == '__main__':

    try:
        if os.path.getsize('some_text.txt') <= 0:
            raise EmptyFile
    except OSError as e:
        print(e, 'File is empty or not exist')
    except EmptyFile as am:
        print('File is empty :(')


    s = os.path.getsize('some_text.txt')
    print('File size is', s, 'kb.')
    res = WorkWithText()
    res.number_of_words()
    res.number_of_symbols()
    res.num_of_symbols_without_spaces()
    res.amount_of_sentence()
    res.how_many_points()
    res.how_many_numbers()
    res.how_many_dashes()
    res.amount_of_strings()
    print(res)


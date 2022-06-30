# 1. Create a class that performs statistical processing of a text file - counting characters, words, sentences, etc.
# Determine the required attributes-data and attributes-methods in class for working with the text file.
import os
from exception_for_text import EmptyFile

class WorkWithText:

    def __init__(self, text):
        self.text = text

    def number_of_words(self):
        return self.text.count(' ')

    def amount_of_strings(self):
        count = 0
        for i in self.text:
            if '\n' in i:
                count += 1
        return count

    def number_of_symbols(self):
        return len(self.text)

    def num_of_symbols_without_spaces(self):
        return len(self.text) - self.text.count(' ')

    def amount_of_sentence(self):
        return len(self.text.split('. ')) + 1

    def how_many_points(self):
        return self.text.count('.')

    def how_many_numbers(self):
        count = 0
        for number in self.text:
            if number.isdigit():
                count += 1
        return count

    def how_many_dashes(self):
        count = 0
        for dash in self.text:
            if '-' in dash:
                count += 1
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
        with open('some_text.txt', 'r') as f:
            data = f.read()
    except OSError as e:
        print(e, 'File is empty or not exist')
    except EmptyFile as am:
        print('File is empty :(')


    s = os.path.getsize('some_text.txt')
    print('File size is', s, 'kb.')
    res = WorkWithText(data)
    res.number_of_words()
    res.number_of_symbols()
    res.num_of_symbols_without_spaces()
    res.amount_of_sentence()
    res.how_many_points()
    res.how_many_numbers()
    res.how_many_dashes()
    res.amount_of_strings()
    print(res)
    print(data)


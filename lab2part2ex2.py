"""
Task 2.
Create a class that performs statistical processing of a text file - counting characters, words, sentences, etc.
Determine the required attributes-data and attributes-methods in class for working with the text file.
"""

import re


class TextProcessor(object):
    """ Class TextProcessor performs statistical processing of a text file - counting characters,
     words, sentences, special characters by using appropriate methods."""

    @staticmethod
    def process_characters():
        file = open('textFileForEx2Lab2.txt')
        text = file.read()
        file.close()
        return len(text)

    @staticmethod
    def count_special_characters(symbol):
        file = open('textFileForEx2Lab2.txt')
        text = file.read()
        file.close()
        return text.count(symbol)

    @staticmethod
    def process_words():
        file = open('textFileForEx2Lab2.txt')
        text = file.read()
        file.close()
        return len(text.split())

    @staticmethod
    def process_sentences():
        file = open('textFileForEx2Lab2.txt')
        text = file.read()
        file.close()
        result = re.split(r"[.?!\n]+", text)
        return len(list(filter(lambda x: x, result)))

    @staticmethod
    def show_text():
        file = open('textFileForEx2Lab2.txt')
        text = file.read()
        file.close()
        return text


# print(TextProcessor.show_text())
print("Number of all characters:", TextProcessor.process_characters())
print("Number of ',' symbols:", TextProcessor.count_special_characters(','))
print("Number of '.' symbols:", TextProcessor.count_special_characters('.'))
print("Number of ':' symbols:", TextProcessor.count_special_characters(':'))
print("Number of '?' symbols:", TextProcessor.count_special_characters('?'))
print("Number of '!' symbols:", TextProcessor.count_special_characters('!'))
print("Number of all words:", TextProcessor.process_words())
print("Number of all sentences:", TextProcessor.process_sentences())

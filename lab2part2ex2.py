"""
Task 2.
Create a class that performs statistical processing of a text file - counting characters, words, sentences, etc.
Determine the required attributes-data and attributes-methods in class for working with the text file.
"""

import re


class TextProcessor(object):
    def __init__(self, file_to_check):
        self._characters = 0
        self._words = 0
        self.text = file_to_check.read()

    def process_characters(self):
        return len(self.text)

    def count_special_characters(self, symbol):
        return self.text.count(symbol)

    def process_words(self):
        return len(self.text.split())

    def process_sentences(self):
        result = re.split(r"[.?!\n]+", self.text)
        return len(list(filter(lambda x: x, result)))


file = open('C:/Users/Kolya/Desktop/OOP_python_LR/textFileForEx2Lab2.txt')
new_text = TextProcessor(file)
# print(new_text.text)
print("Number of all characters:", new_text.process_characters())
print("Number of ',' symbols:", new_text.count_special_characters(','))
print("Number of '.' symbols:", new_text.count_special_characters('.'))
print("Number of ':' symbols:", new_text.count_special_characters(':'))
print("Number of '?' symbols:", new_text.count_special_characters('?'))
print("Number of '!' symbols:", new_text.count_special_characters('!'))
print("Number of all words:", new_text.process_words())
print("Number of all sentences:", new_text.process_sentences())

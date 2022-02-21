"""Word Finder: finds random words from a dictionary."""
from random import choice


# class WordFinder:
#     def __init__(self, file):
#         self.words = []
#         self.file = file

#         words_file = open(file, "r")
#         for word in words_file:
#             self.words.add(word)

#     def __repr__(self):
#         word_count = len(self.words)
#         return f"{word_count} words read"

#     def random(self):

    

class WordFinder:

    def __init__(self, file):
        """
        Open and read txt file.
        Use list_words() to add all words in file to a list.
        Print the number of words in the file.
        """

        word_file = open(file)
        self.words = self.list_words(word_file)
        word_file.close()

        word_count = len(self.words)
        print(f"{word_count} words read in file")
    

    def list_words(self, word_file):
        """Add each word from word file into list"""

        return [word.strip() for word in word_file]

    
    def random(self):
        """Return random word from list"""
        return choice(self.words)

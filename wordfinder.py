"""Word Finder: finds random words from a dictionary."""
from random import choice
    

class WordFinder:
    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("colors.txt")
    4 words read

    >>> wf
    WordFinder file = colors.txt 

    >>> wf.random()
    yellow

    >>> wf.random() in ['blue', 'green', 'yellow', 'red']
    True
    """

    def __init__(self, file):
        """
        Open and read txt file.
        Use list_words() to add all words in file to a list.
        Print the number of words in the file.
        """

        word_file = open(file)
        self.file = file
        self.words = self.list_words(word_file)
        word_file.close()

        word_count = len(self.words)
        print(f"{word_count} words read in file")
    

    def __repr__(self):
        return f"WordFinder file = {self.file}"


    def list_words(self, word_file):
        """Add each word from word file into list"""

        return [word.strip() for word in word_file]

    
    def random(self):
        """Return random word from list"""

        return choice(self.words)


class SpecialWordFinder(WordFinder):
    """
    Specialized WordFinder that ignores blank lines and comments.

    >>> swf = SpecialWordFinder("complex.txt")
    8 words read

    >>> swf
    WordFinder file = complext.txt 

    >>> swf.random()
    yellow

    >>> swf.random() in ['blue', 'green', 'yellow', 'red']
    True
    """
    
    def __init__(self, file):
        super().__init__(file)

    
    def list_words(self, word_file):
        """Add each word from word file into list, skipping blanks and comments"""
        return [word.strip() for word in word_file if word.strip() and not word.startswith('#')]


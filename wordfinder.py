"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    """Machine to pull random words from a file at a specified path."""

    def __init__(self, path):
        file = open(path,'r')
        temp = {line.strip() for line in file}
        file.close()
        temp.discard('')
        self.words = list(temp)
        print(f'{len(self.words)} words read')
    
    def random(self):
        return choice(self.words)

class SpecialWordFinder(WordFinder):
    """Machine to pull random words from a file at a specified path, but with the ability to ignore lines beginning with '#'"""

    def __init__(self, path):
        super().__init__(path)
        temp = {'#' if word[0] == '#' else word for word in self.words}
        temp.discard('#')
        self.words = list(temp)
        print(f'Original word list is now {len(self.words)} after special characters were ignored')
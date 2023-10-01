import random


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self):
        """read random word file and print out number of words read"""
        self.word_list = WordFinder.read_file()
        num_of_words_read = len(self.word_list)
        print(f"{num_of_words_read} words read")

    @staticmethod
    def read_file():
        """read the entire file containing the random words and return list of words"""
        file = open("words.txt")
        text = file.read()
        file.close()
        return text.split('\n')

    def random(self):
        """return random word"""
        print(random.choice(self.word_list))

class SpecialWordFinder(WordFinder):
    """Special Word Finder: finds random word from file that contains words, spaces and comments"""
    @staticmethod
    def read_file():
        """read the entire file containing the random words, spaces, and comments and return list of words only"""
        new_list = []
        special_list = WordFinder.read_file()
        for line in special_list:
            if (line or not line.beginswith('#')):
                new_list.append(line)
        return new_list
        





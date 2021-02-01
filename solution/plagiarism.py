import os
from string import punctuation

class PlagiarismDetector:
    """
        PlagiarismDetector calculates the percentage of a target plagiarized off source.
    """

    DEFAULT_TUPLE_SIZE = 3

    #THIS_FOLDER = os.path.dirname(os.path.abspath('Plagiarism-Detection/problem/test/test')) 
    
    #print(os.listdir(THIS_FOLDER))


    def __init__(self, file1, file2, synonyms, tuple_size):
        """
        Initializes the PlagiarismDetector Class.

        :param file1: target file to be checked
        :param file2: source file used to check target file
        :param synonyms: a file of synonyms list
        :param tuple_size: the size of the desired n tuple
        """
        if tuple_size <= 0:
            raise Exception("Tuple size must be greater than 0")

        self.tuple_size = tuple_size
        self.synonyms = self.create_synonym_map(synonyms)
        self.source = self.list_to_n_tuple(file1)
        self.target = self.list_to_n_tuple(file2)

    def tokenize_file_to_list(self, file):
        """
        Tokenize a file to a list of words.

        :param file: the file to be converted
        :return: a list with all the words in the file
        """
        file_to_words = []
        with open(file, 'r') as f:
            for line in f:
                file_to_words += line.split()

        if len(file_to_words) < self.tuple_size:
            raise Exception("Tuple is greater than the list of words in file")

        return file_to_words

    def create_synonym_map(self, synonym_file):
        """
        Create a map with all the possible synonyms as keys and have their first respective synonym according to the
        word as a value of the key.

        :param synonym_file: a file containing a list of synonyms
        :return: the dictionary where the key is the synonym and value is the first synonym

        """
        synonyms = {}
        with open(synonym_file, 'r') as f:
            for line in f:
                words = line.split()
                for word in words:
                    word = self.clean_data(word)
                    synonyms[word] = words[0]
        return synonyms

    def list_to_n_tuple(self, file):
        """
        Converts a file to a list of n tuples.

        :param file: the file to be converted
        :return: a list of tuples
        """
        words = self.tokenize_file_to_list(file)

        # if word is in synonyms replace word with the value
        for i, word in enumerate(words):
            if words[i] in self.synonyms:
                words[i] = self.synonyms[word]
            words[i] = self.clean_data(words[i])

        list_n_tuple = []
        for i in range(len(words) - self.tuple_size + 1):
            list_n_tuple.append(tuple(words[i:i + self.tuple_size]))
        return list_n_tuple

    def clean_data(self, str):
        """
        Sanitize input data before parsing

        :param str: word
        :return: string in lowercase and without punctuations
        """
        return str.lower().translate(str.maketrans('', '', punctuation))

    def get_plagiarized_percentage(self):
        """
        Calculates the percentage a file is plagiarized

        :return: a percentage ranging from 0 to 100
        """
        plagiarized = 0
        for set_of_words in self.target:
            if set_of_words in self.source:
                plagiarized += 1

        return plagiarized / len(self.target) * 100 if plagiarized is not 0 else 0

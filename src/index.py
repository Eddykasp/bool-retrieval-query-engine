import pickle


class InvertedIndex:
    """Represents an inverted index of words with document occurrences
    and positions of occurrences.
    """
    index = {}

    def read_index_from_file(self, filepath):
        """Reads stored index from file using pickle.  This has to be
        a trusted file."""
        file = open(filepath, "rb")
        index = pickle.load(file, fix_imports=False)
import string
from stemming.porter2 import stem


class BowDocument:
    """
    Part answer of Q1
    for build the document object
    include document ID, length and terms information
    """

    def __init__(self, id):  # constructor
        self.__ID = id
        self.__terms = {}
        self.__docLength = 0

    def get_length(self):
        return self.__docLength

    def set_length(self, doc_length):
        self.__docLength = doc_length

    def get_id(self):
        return self.__ID

    def set_id(self, doc_id):
        self.__ID = doc_id

    def get_terms(self):
        return self.__terms

    # for count terms in document
    def add_terms(self, terms):
        try:
            self.__terms[terms] += 1
        except KeyError:
            self.__terms[terms] = 1

    @staticmethod
    def parse_doc(input_path, stop_ws):
        """
        For parse document and this is the basic function of whole assignment
        :param input_path: the path of input files
        :param stop_ws: the list of stop words
        :return:
        """
        file = open(input_path)
        start_end = False
        files = file.readlines()
        doc_length = 0  # count how many words in one doc after stemming
        doc_id = 0  # initialize the doc ID
        document = BowDocument(doc_id)  # initialize the document object
        # the whole for loop is for get text from files and stem them
        for line in files:
            line = line.strip()
            # the first if part is to get doc ID
            if not start_end:
                if line.startswith("<newsitem "):
                    for part in line.split():
                        if part.startswith("itemid="):
                            doc_id = part.split("=")[1].split("\"")[1]  # get doc ID form the file
                            document.set_id(doc_id)
                            break
                if line.startswith("<text>"):
                    start_end = True
            elif line.startswith("</text>"):
                break
            # the else part is to stem the words
            else:
                line = line.replace("<p>", "").replace("</p>", "")
                line = line.translate(str.maketrans('', '', string.digits)).translate(
                    str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
                line = line.replace("\\s+", " ")
                for term in line.split():
                    doc_length += 1
                    term = stem(term)
                    term = term.lower()
                    if len(term) > 2 and term not in stop_ws:
                        document.add_terms(term)  # put term in addTerms method
        file.close()
        document.set_length(doc_length)  # set the length of the document
        return document

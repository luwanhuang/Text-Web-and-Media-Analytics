import math
import string
from stemming.porter2 import stem


def calculate_average_length(documents):
    """
    To calculate average length of all doc
    :param documents: the set of documents
    :return: average length of all doc
    """
    total = 0
    total_documents = 0
    for doc in documents.items():  # dict.items()
        total_documents += 1
        total += doc[1].get_length()
    return int(total / total_documents)


def print_doc_length(documents):
    """
    To print out the length of each document and average length
    :param documents:
    :return:
    """
    print("The document's length:")
    for document in documents.values():
        print("Document: %s, Length: %d" % (document.get_id(), document.get_length()))
    print("the average length is " + str(calculate_average_length(documents)))


def calculate_BM25(documents, query):
    """
    To calculate the BM25
    :param documents: the set of documents
    :param query: one query of the string list from the user
    :return: the dictionary of doc and BM25 score
    """
    ave_length = calculate_average_length(documents)    # get average length of doc set
    # from line 43 to 54, this part is to stem the query
    query = query.translate(str.maketrans('', '', string.digits)).translate(
        str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
    query = query.replace("\\s+", " ")
    bm25_list = {}  # the query score
    term_number = {}  # to count the num of each word in query
    for term in query.split():
        term = stem(term)
        term = term.lower()  # wk3
        try:
            term_number[term] += 1
        except KeyError:
            term_number[term] = 1
    # this for loop is to calculate the tf*idf
    for term in term_number:
        for doc in documents.items():  # dict.items()
            total_words = 0  # total words in one document
            num = 0  # the number of this words in one document
            doc_id = doc[0]  # key
            document = doc[1]  # value
            term_list = document.get_terms()  # the total amount of terms. term_list => variable name of document.terms
            for i in term_list:
                total_words += term_list[i]
                if term == i:
                    num = term_list[i]
            total = 0  # how many documents include this word
            for docs in documents.items():  # dict.items()
                if term in docs[1].get_terms():
                    total += 1
            part1 = math.log((0 + 0.5) / 0.5 / ((total + 0.5) / (len(documents) - total + 0.5)))
            part2 = (1.2 + 1) * num / (1.2 * ((1 - 0.75) + (0.75 * (total_words / ave_length))) + num)
            part3 = (100 + 1) * term_number[term] / (100 + term_number[term])
            bm25 = part1 * part2 * part3
            try:
                bm25_list[doc_id] += bm25
            except KeyError:
                bm25_list[doc_id] = bm25
    sorted_x = sorted(bm25_list.items(), key=lambda kv: kv[1], reverse=True)    # sort and reverse the list
    print("Average document length " + str(ave_length) + " for query: " + query)
    for x, y in sorted_x:
        print("Document: %s, Length: %d and BM25 Score: %6f" % (x, documents[x].get_length(), y))
    return sorted_x


def ranking_bm25(documents, line):
    """
    To rank the BM25 score
    :param documents:
    :param line:
    :return:
    """
    ave_length = calculate_average_length(documents)
    fo = open("../outputdata/YunfangZhang_Q3.txt", "w")
    for i in line:
        print('=' * 50)
        fo.write('=' * 50 + '\n')
        score_list = calculate_BM25(documents, i)   # use calculate_BM25 method to get score
        m = 0   # for print top 3 BM25 score in the list
        print('For query "%s", three recommended relevant documents and their BM25 score:' % i)
        fo.write("Average document length %d for query: %s \n" % (ave_length, i))
        for x, y in score_list:
            fo.write("Document: %s, Length: %d and BM25 Score: %6f\n" % (x, documents[x].get_length(), y))
        fo.write('For query "%s", three recommended relevant documents and their BM25 score:\n' % i)
        for x, y in score_list:
            if m < 3:
                fo.write("%s : %6f\n" % (x, y))
                print("%s : %6f" % (x, y))
                m += 1

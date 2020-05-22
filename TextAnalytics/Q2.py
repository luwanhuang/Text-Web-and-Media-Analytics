import math


def total_frequency(documents):
    """
    To calculate the document frequency
    :param documents: the set of documents
    :return:
    """
    fo = open("../outputdata/YunfangZhang_Q2a.txt", "w")
    total_list = {}
    count_document = 0
    # the for loop is to count the df of every words
    for doc in documents.items():  # dict.items()
        count_document += 1
        term_list = doc[1].get_terms()  # the term list of every doc
        # if list has this word then add 1, else will record it and let it = 1
        for i in term_list:
            try:
                total_list[i] += 1
            except KeyError:
                total_list[i] = 1
    sorted_x = sorted(total_list.items(), key=lambda kv: kv[1],
                      reverse=True)  # sort and reverse the list
    print('=' * 50)
    fo.write('=' * 50 + '\n')
    print('There are %d documents in this data set and contains %d terms:' % (count_document, len(total_list)))
    fo.write('There are %d documents in this data set and contains %d terms:\n' % (count_document, len(total_list)))
    # display the information
    for x, y in sorted_x:
        print("%s: %d" % (x, y))
        fo.write("%s: %d" % (x, y))
        fo.write('\n')
    fo.write('\n')
    fo.close()


def calculate_tfidf(documents):
    """
    To calculate tf*idf
    :param documents: the set of documents
    :return: a dictionary of each file, key is terms and value is its tf*idf
    """
    doc_dictionary = {}
    fo = open("../outputdata/YunfangZhang_Q2b.txt", "w")
    for doc in documents.items():  # dict.items()
        m = 0   # for print top 20 list in for loop
        total_idf = 0
        tfidf_dictionary = {}   # a dictionary of each file, key is terms and value is its tf*idf
        docID = doc[0]  # get doc ID
        document = doc[1]  # get doc object
        term_list = document.get_terms()  # get list for iterate
        for i in term_list:
            total = 0  # total documents include the word
            for docs in documents.items():  # dict.items()
                list1 = docs[1].get_terms()
                if i in list1:
                    total += 1
            tfidf_dictionary[i] = (1 + math.log(term_list[i])) * (math.log(len(documents) / total))
            total_idf += tfidf_dictionary[i] ** 2
        for i in tfidf_dictionary:
            tfidf_dictionary[i] = tfidf_dictionary[i] / math.sqrt(total_idf)
        print('=' * 50)
        fo.write('=' * 50 + '\n')
        print('Document ' + docID + ' contains ' + str(len(term_list)) + ' terms.')
        fo.write('Document ' + docID + ' contains ' + str(len(term_list)) + ' terms.\n')

        sorted_x = sorted(tfidf_dictionary.items(), key=lambda kv: kv[1],
                          reverse=True)  # term_list.items() => dict.items() =>print items in the dictionary
        doc_dictionary[docID] = tfidf_dictionary
        for x, y in sorted_x:
            if m < 20:
                print("%s: %6f" % (x, y))
                fo.write("%s: %6f" % (x, y))
                fo.write('\n')
            m += 1
    fo.close()
    return doc_dictionary

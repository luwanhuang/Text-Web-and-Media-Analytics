#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import Q2
import Q3
import BowDocument as Bo


def display_doc_info(document):
    """
    Display document ID and how many terms included
    and how many of each term
    :param document:the documents set after stemming
    :return:
    """
    fo = open("../outputdata/YunfangZhang_Q1.txt", "w")
    for doc in document.items():  # dict.items()
        docID = doc[0]  # get document ID
        document = doc[1]  # get document object
        term_list = document.get_terms()  # get term list for sort and iterate
        print('=' * 50)
        fo.write('=' * 50 + '\n')
        print('Document %s contains: %s terms (stems)  and have total %s words'
              % (docID, len(term_list), document.get_length()))
        fo.write('Document %s contains: %s terms (stems)  and have total %s words\n'
                 % (docID, len(term_list), document.get_length()))
        sorted_x = sorted(term_list.items(), key=lambda kv: kv[1],
                          reverse=True)  # sort the list and reverse the order
        for x, y in sorted_x:
            print("%s: %d" % (x, y))
            fo.write("%s: %d" % (x, y))
            fo.write('\n')
        fo.write('\n')
    fo.close()


if __name__ == '__main__':
    file = open('common-english-words.txt', mode='r')
    stopWords = file.read().split(',')  # get stop words list
    file.close()
    inputData = os.getcwd()+'\\inputdata'   # use relative path to make sure this assignment can work on tutor's PC
    listOfDoc = {}  # the dictionary for documents
    os.chdir(inputData)
    a = Bo.BowDocument('')  # initialisation
    for f in os.listdir(inputData):  # f = each file in directory
        d = a.parse_doc(f, stopWords)  # d = myDoc
        if d.get_id() != '':
            listOfDoc[d.get_id()] = d
    display_doc_info(listOfDoc)    # Q1
    Q2.total_frequency(listOfDoc)    # Q2a
    Q2.calculate_tfidf(listOfDoc)    # Q2b
    Q3.print_doc_length(listOfDoc)   # Q3a
    Q3.calculate_BM25(listOfDoc, "stock market")  # Q3c
    # the line is a list and for user to change query as they like
    line = ["British fashion", "fashion awards", "Stock market", "British Fashion Awards"]
    Q3.ranking_bm25(listOfDoc, line)   # Q3d





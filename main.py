import nltk
import math
from nltk.tokenize.treebank import TreebankWordDetokenizer
import standardize
import QandA

qna_lst = standardize.qna_lst
detokenizer = TreebankWordDetokenizer()

def make_QandA_lst(qna_lst):
    QandA_lst = []     # a list stores all class variable of QandA
    for qna in qna_lst:
        new_QandA = QandA.QandA(qna[0], nltk.word_tokenize(qna[1]), qna[2])
        QandA_lst.append(new_QandA)
        
    return QandA_lst

def count_occur(QandA_lst):     # count the occurance of certain word in all query
        occur = {}
        for qna in QandA_lst:
            word_lst = set(qna.que)     # remove repetition
            for word in word_lst:
                if not (word in occur):
                    occur[word] = 1
                else:
                    occur[word] = occur[word] + 1
        return occur

def get_tfidf(QandA_lst):
    for qna in QandA_lst:
        for word in qna.que:
            tf = qna.que.count(word)
            tf = tf/len(qna.que)
            idf = math.log((len(QandA_lst) / occur[word]))
            qna.tfidf[word]= tf*idf 


QandA_lst = make_QandA_lst(qna_lst)     # the list stores all class variable of QandA
occur = count_occur(QandA_lst)
get_tfidf(QandA_lst)
